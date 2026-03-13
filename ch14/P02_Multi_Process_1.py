"""
    该案例演示了进程对象的创建方式1 multiprocessing.Process
    需求：同时对文件进行读写操作
"""
import multiprocessing
import time


# 向文件中写入数据
def write_file():
    with open("test.txt", "a") as f:
        while True:
            f.write("hello world\n")
            # 手动将缓冲区数据刷写到文件中
            f.flush()
            time.sleep(0.5)

# 从文件中读取数据
def read_file():
    with open("test.txt", "r") as f:
        while True:
            time.sleep(0.5)
            print(f.readline())

if __name__ == '__main__':
    # 如果用前面掌握的知识，没有办法让上面两个函数同时执行
    # 需要创建两个进行，分别用于读写文件
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    p1.start()
    p2.start()