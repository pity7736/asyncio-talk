import uvicorn


if __name__ == '__main__':
    uvicorn.run('asyncio_talk:async_app', port=8001)
