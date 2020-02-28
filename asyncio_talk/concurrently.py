import asyncio
import time

import uvloop

import httpx

from common import sites, async_request, async_request2, sync_request


async def async_main():
    loop = asyncio.get_event_loop()
    # loop = uvloop.new_event_loop()
    # asyncio.set_event_loop(loop)
    tasks = (asyncio.create_task(async_request(url, loop)) for url in sites)
    init = loop.time()
    await asyncio.gather(*tasks)
    print(f'total time elapsed: {loop.time() - init}')


async def async_main2():
    # loop = asyncio.get_event_loop()
    loop = uvloop.new_event_loop()
    init = loop.time()
    asyncio.set_event_loop(loop)
    client = httpx.AsyncClient()
    tasks = (asyncio.create_task(async_request2(client, url, loop)) for url in sites)
    await asyncio.gather(*tasks)
    await client.aclose()
    print(f'total time elapsed: {loop.time() - init}')


def sync_main():
    init = time.monotonic()
    list(map(sync_request, sites))
    print(f'total time elapsed: {time.monotonic() - init}')


if __name__ == '__main__':
    import sys
    arg = sys.argv[1]
    if arg == 'sync':
        sync_main()
    elif arg == 'async2':
        asyncio.run(async_main2())
    else:
        asyncio.run(async_main())
