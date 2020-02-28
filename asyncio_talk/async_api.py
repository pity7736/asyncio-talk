import asyncio
import time
from concurrent.futures.process import ProcessPoolExecutor

from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route

from asyncio_talk.common import async_request, sync_request


async def index(request):
    return JSONResponse({'hello': 'word'})


async def arequest(request):
    print('async request')
    loop = asyncio.get_event_loop()
    r = await async_request('https://www.google.com', loop)
    await asyncio.sleep(10)
    return PlainTextResponse(str(r.status_code == 200))


async def srequest(request):
    print('sync request')
    r = sync_request('https://www.google.com')
    time.sleep(4)
    return PlainTextResponse(str(r.status_code == 200))


def cpu_bound():
    time.sleep(5)


async def blocking(request):
    print('doing cpu bound process')
    cpu_bound()
    return PlainTextResponse('ok')


async def blocking_pool(request):
    print('doing cpu bound process pool')
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor(max_workers=5) as pool:
        await loop.run_in_executor(pool, cpu_bound)
    return PlainTextResponse('ok')


async_app = Starlette(debug=True, routes=(
    Route('/', index),
    Route('/request', arequest),
    Route('/sync-request', srequest),
    Route('/blocking', blocking),
    Route('/blocking-pool', blocking_pool),
))
