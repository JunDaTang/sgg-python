"""
    该案例演示了线程安全问题
"""
import threading
import time


def func():
    global g_num
    for _ in range(10):
        lock.acquire()  # 获取 锁
        # g_num += 1
        # g_num = g_num +1
        tmp = g_num + 1
        time.sleep(0.01)
        g_num = tmp
        print(f"当前线程{threading.current_thread().name}",g_num)
        lock.release()


if __name__ == '__main__':
    g_num = 0
    # 创建线程对象
    lock = threading.Lock()
    threads = [threading.Thread(target=func,name="线程" + str(i)) for i in range(1,4)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print(f"当前线程{threading.current_thread().name}",g_num)
