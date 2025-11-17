# セマフォを使って２つのスレッドが占有可能な状態にする
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# １つ目のスレッドで実行する処理の中身
def worker1(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


# 3つ目のスレッドで実行する処理の中身
def worker3(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


if __name__ == "__main__":
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()
    print("started")
