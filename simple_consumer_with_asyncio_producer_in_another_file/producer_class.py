#!/usr/bin/env python
import asyncio
from abc import ABCMeta

import aiohttp
import faust


class Producer:
    app = faust.App('concurrency', broker='kafka://localhost:9092')
    topic = app.topic('concurrency')

    @staticmethod
    @app.agent(topic, concurrency=200)
    async def mytask(records):
        session = aiohttp.ClientSession()
        async for record in records:
            await session.get(f'http://www.google.com/?#q={record.value}')

    async def producer(self):
        for i in range(10_000):
            await self.topic.send(value=i)
