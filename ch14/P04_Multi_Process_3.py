"""
    该案例演示创建进程对象方式3   通过进程池创建进程对象
"""
import multiprocessing
import os
import time


def func():
    for i in range(10):
        print(os.getpid(), i,multiprocessing.current_process())
        time.sleep(0.2)

if __name__ == '__main__':
    process_num = 3
    pool = multiprocessing.Pool(process_num)

    for _ in range(process_num):
        # 将任务交给进程池中的进程执行
        # pool.apply(func) # 同步  阻塞
        pool.apply_async(func)  # 异步  非阻塞

    pool.close()
    pool.join()
    print(f"当前进程名字{multiprocessing.current_process().name}:end")

