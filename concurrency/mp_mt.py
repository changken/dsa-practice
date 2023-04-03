from multiprocessing import Process
import threading
import time


def AnotherThread(id):
    print("tid{id}".format(id=id))
    for i in range(10):
        print(id + i)
        time.sleep(1)


def AnotherProcess(id):
    print("pid{id}".format(id=id))
    for i in range(10):
        print(id + i)
        time.sleep(1)


if __name__ == "__main__":
    id = 1
    t = threading.Thread(target=AnotherThread, args=[id])
    p = Process(target=AnotherProcess, args=[id])

    t.start()
    p.start()

    t.join()
    p.join()

print('end')
