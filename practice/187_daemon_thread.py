import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# １つ目のスレッドで実行する処理の中身
def worker1(lock):
    with lock:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(lock):
    with lock:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


# 3つ目のスレッドで実行する処理の中身
def worker3(lock):
    with lock:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


if __name__ == "__main__":
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(lock,))
    t2 = threading.Thread(target=worker2, args=(lock,))
    t3 = threading.Thread(target=worker3, args=(lock,))
    t1.start()
    t2.start()
    t3.start()
    print("started")
