# 1. スレッドの処理を待たずにプログラムを終了する
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# １つ目のスレッドで実行する処理の中身
def worker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2():
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


if __name__ == "__main__":
    t1 = threading.Thread(target=worker1)
    # スレッド1の結果を待たず、プログラムを終了する
    t1.daemon = True
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print("started")
