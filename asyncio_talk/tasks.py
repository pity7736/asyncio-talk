import asyncio
from .coro import coro


async def main():
    task = asyncio.create_task(coro(5))
    await task
    print('sleep main')
    await asyncio.sleep(3)
    print('finish!')


asyncio.run(main())
