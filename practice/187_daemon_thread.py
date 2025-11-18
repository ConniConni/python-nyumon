# 3つのスレッド分散処理して処理を実行する
import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# 1つ目のスレッドで実行する処理の中身
def worker1(queue):
    logging.debug("start")
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(queue):
    logging.debug("start")
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug("end")


if __name__ == "__main__":
    queue = queue.Queue()
    for i in range(100000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        # t2 = threading.Thread(target=worker2, args=(queue,))
        t.start()
        # t2.start()
        # print("started")
        ts.append(t)
    logging.debug("tasks are not done")
    queue.join()
    logging.debug("tasks are done")
    for _ in range(len(ts)):
        queue.put(None)
    [t.join() for t in ts]
