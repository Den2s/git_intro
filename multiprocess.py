from multiprocessing import Process, Pipe
import time


def f(conn,tm):
    time.sleep(tm)
    conn.send([42, None, 'hello', tm])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,10 ,))
    p2 = Process(target=f, args=(child_conn,5 ,))
    p.start()
    p2.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
    p2.join()
