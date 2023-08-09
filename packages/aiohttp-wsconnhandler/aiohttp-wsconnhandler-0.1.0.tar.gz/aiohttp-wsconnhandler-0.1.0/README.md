# aiohttp-wsconnhandler

The package implements the `WSConnectionHandler` class that provides receive and send queues when handling WebSocket communication with aiohttp.

## Work-in-Progress

The repository contains a module extracted from my other project and was refactored as a separate package.

Currently, the plan is to rewrite it as a "general purpose" module that could be used in other WebSocket client and server apps.

## Usage Examples

### WebSocket Client

```
from aiohttp_wsconnhandler import WSConnectionHandler

...
```

### WebSocket Server

```
from aiohttp_wsconnhandler import WSConnectionHandler

...
```