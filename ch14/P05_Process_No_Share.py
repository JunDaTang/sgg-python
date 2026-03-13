"""
    该案例演示了进程间不能共享全局变量
"""
import multiprocessing
import os
import time


def func(list1):
    for i in range(10):
        list1.append(i)
        print(os.getpid(), list1)


if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func,args=(list1,))
    p2 = multiprocessing.Process(target=func,args=(list1,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"当前进程名{multiprocessing.current_process().name}",list1)
