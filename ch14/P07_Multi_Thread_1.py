"""
    该案例演示了线程创建的方式1   threading.Thread()
"""
import multiprocessing
import threading
import time


# 两线程分别交替打印
def func():
    flag = 0
    while True:
        print(f"线程{threading.current_thread().name}",f"{flag}" * 5)
        flag = flag ^ 1
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)

    t1.start()
    t2.start()

    # p1 = multiprocessing.Process(target=func)
    # p2 = multiprocessing.Process(target=func)
    # p1.start()
    # p2.start()