import time


class Iterator:

    def __init__(self, to):
        self._i = 0
        self._to = to

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < self._to:
            self._i += 1
            time.sleep(0.1)
            return self._i
        raise StopIteration
