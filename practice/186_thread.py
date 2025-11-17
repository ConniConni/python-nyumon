# スレッドを２つ立ててみる
import threading
import time


# １つ目のスレッドで実行する処理の中身
def worker1():
    # 現在実行中のスレッドの名前を取得し、start（end）と表示する
    print(threading.current_thread().name, "start")
    time.sleep(3)
    print(threading.current_thread().name, "end")


# 2つ目のスレッドで実行する処理の中身
def worker2():
    # 現在実行中のスレッドの名前を取得し、start（end）と表示する
    print(threading.current_thread().name, "start")
    time.sleep(4)
    print(threading.current_thread().name, "end")


if __name__ == "__main__":
    # 変数にスレッドオブジェクトを代入
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    # スレッド t1 を開始　メインプログラムの流れとは別にworker1関数の実行が始まる
    t1.start()
    t2.start()
    print("started")
