from asyncio import Future
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union

from tornado import httpclient
from tornado.netutil import Resolver
from tornado.websocket import WebSocketClientConnection, websocket_connect


def mstpsocket_connect(
    url: Union[str, httpclient.HTTPRequest],
    callback: Optional[Callable[["Future[WebSocketClientConnection]"], None]] = None,
    connect_timeout: Optional[float] = None,
    on_message_callback: Optional[Callable[[Union[None, str, bytes]], None]] = None,
    compression_options: Optional[Dict[str, Any]] = None,
    ping_interval: Optional[float] = None,
    ping_timeout: Optional[float] = None,
    max_message_size: int = 10 * 1024 * 1024,
    subprotocols: Optional[List[str]] = None,
    resolver: Optional[Resolver] = None,
) -> "Awaitable[WebSocketClientConnection]":
    scheme, sep, rest = url.partition(":")
    scheme = {"mstp": "ws", "mstps": "wss"}[scheme]
    ws_url = scheme + sep + rest

    return websocket_connect(
        ws_url,
        callback=callback,
        connect_timeout=connect_timeout,
        on_message_callback=on_message_callback,
        compression_options=compression_options,
        ping_interval=ping_interval,
        ping_timeout=ping_timeout,
        max_message_size=max_message_size,
        subprotocols=subprotocols,
        resolver=resolver
    )
