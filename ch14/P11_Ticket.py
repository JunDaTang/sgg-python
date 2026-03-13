"""
    该案例演示了线程安全问题
"""
import threading
import time


def sale_ticket():
    global ticket_num

    while True:
        lock.acquire()
        if ticket_num <= 0:
            lock.release()
            break
        time.sleep(0.01)
        ticket_num -= 1
        print(f"当前{threading.current_thread().name}卖了一张票，还剩{ticket_num}")
        lock.release()


if __name__ == '__main__':
    ticket_num = 100
    # 创建线程对象
    lock = threading.Lock()
    threads = [threading.Thread(target=sale_ticket,name="窗口" + str(i)) for i in range(1,4)]
    [t.start() for t in threads]
    [t.join() for t in threads]