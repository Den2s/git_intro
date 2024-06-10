import datetime
from threading import Semaphore, Thread
from time import sleep

s = Semaphore(2)


def semaphore_func(payload: int):
    s.acquire()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'{now=}, {payload=}')
    sleep(2)
    s.release()


threads = [Thread(target=semaphore_func, args=(i,)) for i in range(7)]

for t in threads:
    t.start()

for t in threads:
    t.join()
