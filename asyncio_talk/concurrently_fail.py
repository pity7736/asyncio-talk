import asyncio

from common import sites, wrong_async_request


async def main():
    loop = asyncio.get_event_loop()
    init = loop.time()
    tasks = (asyncio.create_task(wrong_async_request(url)) for url in sites)
    await asyncio.gather(*tasks)
    print(f'total time elapsed: {loop.time() - init}')


asyncio.run(main())
