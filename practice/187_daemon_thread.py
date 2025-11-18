# キューに値を入れる
# 1から9を表示して終了するスレッドを作成する
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
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(queue):
    logging.debug("start")
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug("end")


if __name__ == "__main__":
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)

    t1 = threading.Thread(target=worker1, args=(queue,))
    # t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    # t2.start()
    # print("started")
    logging.debug("tasks are not done")
    logging.debug("tasks are done")
    queue.put(None)
