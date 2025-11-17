# 1. スレッドをLockする
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# １つ目のスレッドで実行する処理の中身
def worker1(d):
    logging.debug("start")
    i = d["x"]
    d["x"] = i + 1
    logging.debug(d)
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(d):
    logging.debug("start")
    i = d["x"]
    d["x"] = i + 1
    logging.debug(d)
    logging.debug("end")


if __name__ == "__main__":
    d = {"x": 0}
    t1 = threading.Thread(target=worker1, args=(d,))
    t2 = threading.Thread(target=worker2, args=(d,))
    t1.start()
    t2.start()
    print("started")
