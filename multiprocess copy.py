from multiprocessing import Process, Manager
import time


def f(d, l):
    time.sleep(10)
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
    print("dd")


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l), daemon=True)
        p.start()
        p.join(5)

        print(d)
        print(l)
