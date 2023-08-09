import asyncio
from dataclasses import asdict, dataclass
import logging
import typing as t


import aiohttp
from aiohttp import web


class WSConnectionHandler:
    """A WebSockets connection handler class

    run_loop() must be called from the task that created aiohttp response
    object.

    In the server code:
    ```
    async def my_handler():
        ...
        my_ws_conn = WSSocketHandler(ws_response)
        await my_ws_conn.run_loop()
        ...
    ```

    In the client code:
    ```
    async def connect_and_loop():
        ...
        async with session.ws_connect(url, **connection_kwargs) as ws:
            my_ws_conn = WSSocketHandler(ws)
            await my_ws_conn.run_loop()
        ...
    ```
    """

    @dataclass
    class Stats:
        n_received: int = 0
        n_receive_format_errors: int = 0
        n_sent: int = 0
        n_send_format_errors: int = 0
        n_ignored: int = 0

    MAX_INVALID_REQUESTS = 5

    _logger: logging.Logger
    _sender_task: asyncio.Task
    _stop_watcher_task: asyncio.Task
    _close_requested: asyncio.Event

    _ws_msg_type: aiohttp.WSMsgType

    @property
    def ws_msg_type(self):
        return self._ws_msg_type

    ws_response: t.Union[aiohttp.ClientWebSocketResponse, web.WebSocketResponse]
    receive_queue: asyncio.Queue
    send_queue: asyncio.Queue

    socket_errors: list[t.Any]
    stats: Stats

    def __init__(
        self,
        ws_response: t.Union[aiohttp.ClientWebSocketResponse, web.WebSocketResponse],
        *,
        logger: logging.Logger = None,
        ws_msg_type: t.Literal[
            aiohttp.WSMsgType.BINARY, aiohttp.WSMsgType.TEXT
        ] = aiohttp.WSMsgType.TEXT,
        receive_queue: asyncio.Queue = None,
        send_queue: asyncio.Queue = None,
    ):
        if not logger:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = logger
        self._close_requested = asyncio.Event()
        self._sender_task = None
        self._stop_watcher_task = None

        assert ws_msg_type in [aiohttp.WSMsgType.BINARY, aiohttp.WSMsgType.TEXT]
        self._ws_msg_type = ws_msg_type

        self.ws_response = ws_response

        if receive_queue is None:
            receive_queue = asyncio.Queue(maxsize=512)
        self.receive_queue = receive_queue

        if send_queue is None:
            send_queue = asyncio.Queue(maxsize=512)
        self.send_queue = send_queue

        self.socket_errors = []
        self.stats = self.Stats()

    def ws_response_repr(self) -> str:
        repr_str = f"{self.ws_response}"
        if isinstance(self.ws_response, web.WebSocketResponse):
            repr_str = f"<WebSocketResponse object at {hex(id(self.ws_response))}>"
        return repr_str

    async def run_loop(self) -> None:
        """Receive and send WebSocket messages"""

        if self.ws_response.closed:
            raise ValueError("socket must not be closed when calling run_loop()")

        log_msg = f"run_loop(): START\n{self.ws_response_repr()}"
        self._logger.info(log_msg)

        self._sender_task = asyncio.create_task(self._run_sender())
        self._stop_watcher_task = asyncio.create_task(self._stop_request_watcher())
        try:
            # According to aiohttp documentation, receiving messages must be
            # performed in the request handler task. Therefore, instead of
            # calling asyncio.create_task(), the reader is awaited in the
            # current task. The reader exits when the connection is closed.
            await self._aloop_reader()
            self._logger.debug("run_loop(): ws_closed")
        except Exception as e:  # pylint: disable=broad-exception-caught
            self._logger.exception("run_loop(): exception", exc_info=e)
            self.socket_errors.append(str(e))
        finally:
            await self._cancel_subtasks()

        stats = asdict(self.stats)
        stats.update({"n_socket_errors": len(self.socket_errors)})
        log_msg = f"run_loop(): DONE\n{self.ws_response_repr()}\n{stats}"
        self._logger.info(log_msg)

    def request_stop(self) -> None:
        self._close_requested.set()

    def _check_msg_format(self, msg: aiohttp.WSMessage) -> bool:
        return msg.type == self.ws_msg_type

    async def _process_received_msg(self, msg: aiohttp.WSMessage) -> None:
        self.stats.n_received += 1
        if not self._check_msg_format(msg):
            self.stats.n_receive_format_errors += 1
            if self.stats.n_receive_format_errors >= self.MAX_INVALID_REQUESTS:
                log_msg = "<incoming_queue status=blocked>"
                self._logger.error(log_msg)
                await self.ws_response.close(message=log_msg)
                return

            return
        try:
            self.receive_queue.put_nowait(msg.data)
        except asyncio.QueueFull:
            log_msg = "<incoming_queue status=blocked>"
            self._logger.error(log_msg)
            await self.ws_response.close(message=log_msg)

    async def _aloop_reader(self) -> None:
        async for msg in self.ws_response:
            if msg.type == aiohttp.WSMsgType.CLOSED:
                log_msg = f"ws_closed '{msg}'"
                self._logger.info(log_msg)
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                log_msg = f"ws_error '{msg}'"
                self._logger.error(log_msg)
                self.socket_errors.append(msg.data)
                break

            if msg.type not in [aiohttp.WSMsgType.BINARY, aiohttp.WSMsgType.TEXT]:
                self.stats.n_ignored += 1
                continue

            await self._process_received_msg(msg)

            if self._sender_task.done():
                break

    async def _aloop_bytes_sender(self) -> None:
        while not self.ws_response.closed:
            data = await self.send_queue.get()
            # log_msg = f"_aloop_bytes_sender()  sent {data}"
            # self._logger.debug(log_msg)
            try:
                await self.ws_response.send_bytes(data)
                self.stats.n_sent += 1
                # log_msg = f"_aloop_bytes_sender():  sent {data}"
                # self._logger.debug(log_msg)
            except ValueError as e:
                self.stats.n_send_format_errors += 1
                self._logger.exception(
                    "_aloop_bytes_sender(): msg is not bytes, bytearray, or memoryview",
                    exc_info=e,
                )
            except RuntimeError as e:
                self._logger.exception(
                    "_aloop_bytes_sender(): connection is not open", exc_info=e
                )

    async def _aloop_str_sender(self) -> None:
        self._logger.debug("_aloop_str_sender(): STARTED")
        while not self.ws_response.closed:
            data = await self.send_queue.get()
            # log_msg = f"_aloop_str_sender()  sent {data}"
            # self._logger.debug(log_msg)
            try:
                await self.ws_response.send_str(data)
                self.stats.n_sent += 1
                # log_msg = f"_aloop_str_sender():  sent {data}"
                # self._logger.debug(log_msg)
            except ValueError as e:
                self.stats.n_send_format_errors += 1
                self._logger.exception(
                    "_aloop_str_sender(): msg is not str", exc_info=e
                )
            except RuntimeError as e:
                self._logger.exception(
                    "_aloop_str_sender(): connection is not open", exc_info=e
                )
        self._logger.debug("_aloop_str_sender(): DONE")

    async def _run_sender(self) -> None:
        if self._ws_msg_type == aiohttp.WSMsgType.BINARY:
            await self._aloop_bytes_sender()
        elif self._ws_msg_type == aiohttp.WSMsgType.TEXT:
            await self._aloop_str_sender()
        else:
            raise ValueError("unsupported ws_msg_type")

    async def _stop_request_watcher(self) -> None:
        await self._close_requested.wait()
        # log_msg = "_stop_request_watcher(): stop_requested, closing ..."
        # self._logger.debug(log_msg)
        await self.ws_response.close()
        # log_msg = "_stop_request_watcher(): stop_requested, closed"
        # self._logger.debug(log_msg)

    async def _cancel_subtasks(self) -> None:
        if self._sender_task.cancel():
            try:
                await self._sender_task
            except asyncio.CancelledError:
                pass
        else:
            self._sender_task.result()

        if self._stop_watcher_task.cancel():
            try:
                await self._stop_watcher_task
            except asyncio.CancelledError:
                pass
