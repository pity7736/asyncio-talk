import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

from common import sync_request, sites


counter = 0
lock = threading.Lock()


def race_conditions():
    global counter
    print('init counter', counter)
    if counter == 3:
        time.sleep(2)
        print('wtf')
    counter += 1
    print('end counter', counter)


def race_conditions_lock():
    with lock:
        global counter
        print('init counter', counter)
        if counter == 3:
            time.sleep(2)
            print('wtf')
        counter += 1
        print('end counter', counter)


def single_thread():
    print('main threading')
    threads = []
    init = time.monotonic()
    for url in sites:
        thread = threading.Thread(target=sync_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'total time elapsed: {time.monotonic() - init}')


def pool():
    print('main pool threading')
    init = time.monotonic()
    with ThreadPoolExecutor(max_workers=len(sites)) as executor:
        executor.map(sync_request, sites)

    print(f'total time elapsed: {time.monotonic() - init}')


def race():
    threads = []
    init = time.monotonic()
    for _ in range(5):
        thread = threading.Thread(target=race_conditions)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'total time elapsed: {time.monotonic() - init}')


def race_lock():
    threads = []
    init = time.monotonic()
    for _ in range(5):
        thread = threading.Thread(target=race_conditions_lock)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'total time elapsed: {time.monotonic() - init}')


if __name__ == '__main__':
    import sys
    try:
        kind = sys.argv[1]
    except IndexError:
        kind = 'single'

    if kind == 'pool':
        pool()
    elif kind == 'race':
        race()
    elif kind == 'lock':
        race_lock()
    else:
        single_thread()
