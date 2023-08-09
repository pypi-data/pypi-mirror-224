"""
Created on 2016/6/20
@author: lijc210@163.com
Desc: 功能描述。
"""
import random
import time
from queue import Queue
from threading import Thread


class ProducerThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        nums = list(range(5))
        while True:
            num = random.choice(nums)
            self.queue.put(num)
            print("Produced", num)
            time.sleep(random.random())


class ConsumerThread(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        while True:
            num = self.queue.get()
            self.queue.task_done()
            print("Consumed", num, self.name)
            time.sleep(random.random())


queue = Queue()
ProducerThread(queue).start()
# ConsumerThread(queue).start()

for x in range(10):
    ConsumerThread(x, queue).start()
