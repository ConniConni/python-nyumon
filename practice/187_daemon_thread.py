# 1. 生存中のスレッドオブジェクトを確認する
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
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.daemon = True
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
