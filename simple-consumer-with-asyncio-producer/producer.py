#!/usr/bin/env python
import asyncio
from abc import ABCMeta

import aiohttp
import faust

app = faust.App('concurrency', broker='kafka://localhost:9092')
topic = app.topic('concurrency')


@app.agent(topic, concurrency=200)
async def mytask(records):
    session = aiohttp.ClientSession()
    async for record in records:
        await session.get(f'http://www.google.com/?#q={record.value}')


async def producer():
    for i in range(10_000):
        await topic.send(value=i)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(producer())
    loop.stop()


if __name__ == '__main__':
    main()
