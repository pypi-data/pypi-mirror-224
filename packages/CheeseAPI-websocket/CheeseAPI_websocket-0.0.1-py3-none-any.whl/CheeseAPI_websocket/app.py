import json

import asyncio
from CheeseAPI.app import app, websocket
from CheeseAPI.request import Request

from CheeseAPI_websocket.websocket import websocket

@app.websocket_beforeConnectionHandle
async def websocket_beforeConnectionHandle():
    if not websocket._async_redis:
        raise ConnectionError('Websocket has not been initialized')

async def _websocket_sendHandle(send, request: Request):
    websocket._CLIENTS.append(request.sid)
    pub = websocket._async_redis.pubsub()
    await pub.subscribe(request.path)
    try:
        while True:
            value = await pub.parse_response()
            if value[0] == b'subscribe':
                continue
            else:
                value = json.loads(value[2])
                flag = False
                if value['sid'] == '*':
                    flag = True
                elif isinstance(value['sid'], list):
                    if request.sid in value['sid']:
                        flag = True
                elif request.sid == value['sid']:
                    flag = True

                if flag:
                    if value['type'] == 'text':
                        await send({
                            'type': 'websocket.send',
                            'text': value['message']
                        })
                    elif value['type'] == 'bytes':
                        await send({
                            'type': 'websocket.send',
                            'bytes': value['message'].encode()
                        })
                    elif value['type'] == 'close':
                        await send({
                            'type': 'websocket.close'
                        })
    except asyncio.CancelledError:
        ...

app._websocket_sendHandle = _websocket_sendHandle
