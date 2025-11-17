# キューに値を入れる
import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# 1つ目のスレッドで実行する処理の中身
def worker1(queue):
    logging.debug("start")
    queue.put(100)
    queue.put(200)
    time.sleep(3)
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(queue):
    logging.debug("start")
    time.sleep(3)
    print(queue.get())
    print(queue.get())
    logging.debug("end")


if __name__ == "__main__":
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue,))
    t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    t2.start()
    print("started")
