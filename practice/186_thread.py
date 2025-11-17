# 1. スレッドを２つ立ててみる
# 2. loggingでスレッドの名前を出力する
# 3. スレッドの名前を変える
# 4. スレッド内で実行する関数に引数を渡す
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


# １つ目のスレッドで実行する処理の中身
def worker1():
    # 現在実行中のスレッドの名前を取得し、start（end）と表示する
    # print(threading.current_thread().name, "start")
    logging.debug("start")
    time.sleep(3)
    # print(threading.current_thread().name, "end")
    logging.debug("end")


# 2つ目のスレッドで実行する処理の中身
def worker2(x, y=1):
    # 現在実行中のスレッドの名前を取得し、start（end）と表示する
    # print(threading.current_thread().name, "start")
    logging.debug("start")
    logging.debug(x)
    logging.debug(y)
    time.sleep(4)
    # print(threading.current_thread().name, "end")
    logging.debug("end")


if __name__ == "__main__":
    # 変数にスレッドオブジェクトを代入
    t1 = threading.Thread(name="rename worker1", target=worker1)
    t2 = threading.Thread(target=worker2, args=(10,), kwargs={"y": 100})
    # スレッド t1 を開始　メインプログラムの流れとは別にworker1関数の実行が始まる
    t1.start()
    t2.start()
    print("started")
