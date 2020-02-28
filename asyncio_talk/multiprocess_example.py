import multiprocessing
import time
from concurrent.futures.process import ProcessPoolExecutor

from common import sync_request, sites


def worker(url):
    # time.sleep(10)
    sync_request(url)


def single():
    print('main multiprocessing')
    threads = []
    init = time.monotonic()
    for url in sites:
        thread = multiprocessing.Process(target=worker, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'total time elapsed: {time.monotonic() - init}')


def pool():
    init = time.monotonic()
    with ProcessPoolExecutor(max_workers=len(sites)) as executor:
        executor.map(worker, sites)

    print(f'total time elapsed: {time.monotonic() - init}')


if __name__ == '__main__':
    import sys
    try:
        kind = sys.argv[1]
    except IndexError:
        kind = 'single'

    if kind == 'pool':
        pool()
    else:
        single()
