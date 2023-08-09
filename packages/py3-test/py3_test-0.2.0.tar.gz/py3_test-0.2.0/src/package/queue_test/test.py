"""
Created on 2017/7/3 0003
@author: lijc210@163.com
Desc: 功能描述。
"""
from queue import Queue
from threading import Thread


class ProducerThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.setDaemon(True)

    def run(self):
        for x in range(100):
            self.queue.put(x)  # 任务加入队列


class ConsumerThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.setDaemon(True)

    def run(self):
        while True:
            data = self.queue.get()  # 取出队列中的数据
            print(data)
            self.queue.task_done()


queue = Queue()
ProducerThread(queue).start()  # 一个生产者
for _x in range(10):  # 十个消费者
    ConsumerThread(queue).start()
