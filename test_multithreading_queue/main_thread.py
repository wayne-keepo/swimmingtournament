from multiprocessing import Process, Lock, Queue
import random


def mult(queue: Queue, lock: Lock):
    while True:
        if not queue.empty():
            print('call que...')
            lock.acquire()
            data = queue.get()
            lock.release()
            print(data)
    # print(queue.get())


def papa(queue: Queue, lock: Lock):
    while True:
        i = random.randint(0, 100)
        k = random.randint(0, 200)
        if i == k:
            lock.acquire()
            queue.put(i)
            lock.release()
            print(i)
        # i = 0

        # print('i: {} qu: {}'.format(i, qu))
        # if i == 23:
        #     return False


if __name__ == '__main__':
    qu = Queue()
    lk = Lock()
    p = Process(target=mult(qu, lk))
    p.daemon = True
    p.start()
    papa(qu, lk)
    p.join()
