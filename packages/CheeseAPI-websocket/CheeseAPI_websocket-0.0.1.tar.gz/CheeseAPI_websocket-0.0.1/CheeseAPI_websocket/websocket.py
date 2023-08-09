import json
from typing import List

import redis, CheeseType, CheeseType.network, CheeseLog
from redis import Redis
from redis.asyncio import Redis as async_Redis

class Websocket:
    def __init__(self):
        self._CLIENTS: List[str] = []
        self._redis: Redis | None = None
        self._async_redis: async_Redis | None = None

    def init(self, host: CheeseType.network.IPv4 = '127.0.0.1', port: CheeseType.network.Port = 6379, db: CheeseType.NonNegativeInt = 0, password: str | None = None, username: str | None = None):
        self._redis = redis.Redis(
            host = host,
            port = port,
            db = db,
            password = password,
            username = username
        )
        self._async_redis = async_Redis(
            host = host,
            port = port,
            db = db,
            password = password,
            username = username
        )

    def send(self, message: any, path: str, sid: str | list[str] | None = None):
        if not self._redis:
            CheeseLog.danger('Websocket has not been initialized')
            return

        if sid is None:
            sid = '*'
        self._redis.publish(path, json.dumps({
            'sid': sid,
            'type': 'bytes' if isinstance(message, bytes) else 'text',
            'message': message
        }).encode())

    async def async_send(self, message: any, path: str, sid: str | list[str] | None = None):
        if not self._redis:
            CheeseLog.danger('Websocket has not been initialized')
            return

        if sid is None:
            sid = '*'
        await self._async_redis.publish(path, json.dumps({
            'sid': sid,
            'type': 'bytes' if isinstance(message, bytes) else 'text',
            'message': message
        }).encode())

    def close(self, path: str, sid: str | list[str] | None = None):
        if not self._redis:
            CheeseLog.danger('Websocket has not been initialized')
            return

        if sid is None:
            sid = '*'
        self._redis.publish(path, json.dumps({
            'sid': sid,
            'type': 'close'
        }).encode())

    async def close(self, path: str, sid: str | list[str] | None = None):
        if not self._redis:
            CheeseLog.danger('Websocket has not been initialized')
            return

        if sid is None:
            sid = '*'
        await self._async_redis.publish(path, json.dumps({
            'sid': sid,
            'type': 'close'
        }).encode())

websocket = Websocket()
