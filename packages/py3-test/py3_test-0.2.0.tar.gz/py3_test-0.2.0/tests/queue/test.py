"""
Created on 2016/6/20
@author: lijc210@163.com
Desc: 功能描述。
"""
import queue
import threading
import time

myqueue = queue.Queue(maxsize=0)  # 队列大小

hosts = ["http://1", "http://2", "http://3", "http://4", "http://5"]
# hosts = ["http://yahoo.com","http://google.com.hk","http://amazon.com","http://ibm.com","http://apple.com"]
queue = queue.Queue()


class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""

    def __init__(self, queue, htint):
        threading.Thread.__init__(self)
        self.queue = queue
        self.Ht = htint  # 线程ID

    def run(self):
        while True:
            # grabs host from queue
            host = self.queue.get()  # get()方法从队头删除并返回一个项目
            print("线程ID %d---%s" % (self.Ht, host))
            print(self.queue.qsize())  # 返回队列的大小，近似值
            if self.queue.empty():  # 如果队列为空
                print("队列为空")
            # grabs urls of hosts and prints first 1024 bytes of page

            #            url = urllib2.urlopen(host)
            #            print url.read(1024)
            # signals to queue job is done
            self.queue.task_done()  # 退出


start = time.time()


def main():
    # spawn a pool of threads, and pass them queue instance
    for i in range(12):
        t = ThreadUrl(queue, i)
        t.setDaemon(True)
        t.start()
        # populate queue with data
        for host in hosts:  # 往线程中填充数据
            queue.put(host)  # 插入队列
        # wait on the queue until everything has been processed
        queue.join()


main()
print("Elapsed Time: %s" % (time.time() - start))
