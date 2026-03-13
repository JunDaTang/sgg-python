"""
    该案例演示了线程对象创建的方式2    定义类继承threading.Thread
"""
import threading
import time


class Worker(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(f"线程{threading.current_thread().name}", f"{flag}" * 5)
            flag = flag ^ 1
            time.sleep(0.5)


if __name__ == '__main__':
    t1 = Worker(name="atguigu-1")
    t2 = Worker(name="atguigu-2")
    t1.start()
    t2.start()