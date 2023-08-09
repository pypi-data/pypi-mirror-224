"""
Created on 2016/6/20
@author: lijc210@163.com
Desc: 功能描述。
"""

import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print("Worker {} got task {}".format(n, task))
        gevent.sleep(0)
        print("Quitting time!")


def boss():
    for i in range(1, 25):
        tasks.put_nowait(i)


gevent.spawn(boss).join()

gevent.joinall(
    [
        gevent.spawn(worker, "fuck shencan"),
        gevent.spawn(worker, "fuck zb"),
        gevent.spawn(worker, "fuck liudehua"),
    ]
)
