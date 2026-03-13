"""
    该案例演示了创建进程对象方式2   创建进程子类   通过子类创建进行对象
"""
import multiprocessing
import os
import time


class Worker(multiprocessing.Process):
    def run(self):
        print(f"当前进程名:{self.name},进程id:{os.getpid()},父进程id:{os.getppid()},name:{__name__}")


if __name__ == '__main__':
    # 创建进程对象
    for i in range(3):
        p = Worker()
        p.start()