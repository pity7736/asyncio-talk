from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def index(request):
    return JSONResponse({'hello': 'word'})


async_app = Starlette(debug=True, routes=(
    Route('/', index),
))
