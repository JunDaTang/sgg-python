"""
    该案例演示了通过Queue实现进程之间的通信
"""
import multiprocessing
import os
import random
import time


# 向队列中放入1~50之间的随机数据，每放入一条，睡眠0.5秒
def func1(qu):
    while True:
        num = random.randint(1, 50)
        qu.put(num)
        print(f"进程{os.getpid()}向队列中放入了{num}")
        time.sleep(0.5)

# 从队列中取出数据
def func2(qu):
    while True:
        # time.sleep(0.5)
        num = qu.get()
        print(f"进程{os.getpid()}从队列中取出了{num}")


if __name__ == '__main__':
    # 创建一个队列对象
    # qu = multiprocessing.Queue()
    qu = multiprocessing.Manager().Queue()

    p1 = multiprocessing.Process(target=func1, args=(qu,))
    p2 = multiprocessing.Process(target=func2, args=(qu,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # qu = multiprocessing.Manager().Queue()
    # pool = multiprocessing.Pool(2)
    # pool.apply_async(func1, args=(qu,))
    # pool.apply_async(func2, args=(qu,))
    # pool.close()
    # pool.join()




