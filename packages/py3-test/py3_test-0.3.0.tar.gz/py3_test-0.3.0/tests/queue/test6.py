"""
Created on 2016/6/20
@author: lijc210@163.com
Desc: 功能描述。
"""
# encoding=utf-8
import threading
import time
from queue import Queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            for _i in range(100):
                if queue.qsize() > 1000:
                    pass
                else:
                    count = count + 1
                    msg = "生成产品" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            for _i in range(3):
                if queue.qsize() < 100:
                    pass
                else:
                    msg = self.name + "消费了 " + queue.get()
                    print(msg)
            time.sleep(1)


queue = Queue()


def test():
    for i in range(500):
        queue.put("初始产品" + str(i))
    for i2 in range(2):
        print(i2)
        p = Producer()
        p.start()
    for i3 in range(5):
        print(i3)
        c = Consumer()
        c.start()


if __name__ == "__main__":
    test()
