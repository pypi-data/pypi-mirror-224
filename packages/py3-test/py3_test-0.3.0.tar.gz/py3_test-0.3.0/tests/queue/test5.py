"""
Created on 2016/6/20
@author: lijc210@163.com
Desc: 功能描述。
"""
import random
import time
from queue import Queue
from threading import Thread

queue = Queue(10)


class ProducerThread(Thread):
    def run(self):
        for x in range(10):
            print(x)
            queue.put(x)
            time.sleep(1)


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print("Consumed", num)
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()

for _i in range(5):
    ConsumerThread().start()
