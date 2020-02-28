import asyncio


class AsyncIterator:

    def __init__(self, to):
        self._i = 0
        self._to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._i < self._to:
            self._i += 1
            await asyncio.sleep(0.1)
            return self._i
        raise StopAsyncIteration
