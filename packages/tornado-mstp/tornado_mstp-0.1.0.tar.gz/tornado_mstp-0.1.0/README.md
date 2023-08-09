# Tornado MSTP

A tornado MSTP library, using WebSocket.

# Installation
`pip install tornado_mstp`

# Easy Examples

See repo's directory named 'examples'.

# Usage

## Server

As a server-side application using `tornado_mstp`. You should first create a 
handler class inherited from `MstpSocketHandler`:
```python
from tornado_mstp import MstpSocketHandler


class MyMstpSocketHandler(MstpSocketHandler):
    pass
```

There are two optional class attributes, `automatic_closing_time`(default to 10) and `ver`(default to "0.1"), that indicate MSTP server information 
need to be set.
```python
from tornado_mstp import MstpSocketHandler


class MyMstpSocketHandler(MstpSocketHandler):
    automatic_closing_time = 15
    ver = "0.1"
```

There is no need to worry about tornado websocket handler's `on_message` method.
Each MSTP package type of message has a callback function who needs to be 
implemented. For example, for segment handling:
```python
from typing import Optional

from tornado_mstp import MstpSocketHandler
from tornado_mstp.schema import ContentType


class MyMstpSocketHandler(MstpSocketHandler):
    automatic_closing_time = 15
    ver = "0.1"

    async def handle_segment(
        self,
        package_id: Optional[str] = None,
        message_index: Optional[int] = None,
        segment_index: Optional[int] = None,
        is_end: Optional[bool] = None,
        content_type: Optional[ContentType] = None,
        content: Optional[str] = None
    ) -> None:
        print(f"received content: {content}")
```

After implementing all callback functions, server can handle any MSTP packages 
as you want.

## Client

As a client-side connection using tornado_mstp. You can just create an 
`mstpsocket_connect` using `tornado_mstp.mstpsocket_connect`. It has the 
same usage of `tornado.websocket.websocket_connect`.

```python
import asyncio
from tornado_mstp import mstpsocket_connect


def callback(message):
    print(message)


async def main():
    conn = mstpsocket_connect(
        url="mstp://other-mstp-server",
        on_message_callback=callback
    )
    await conn


if __name__ == '__main__':
    asyncio.run(main())
```
