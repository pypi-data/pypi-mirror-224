import random
import threading
import time
from queue import Queue


# Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print(
                "%s: %s is producing %d to the queue!"
                % (time.ctime(), self.getName(), i)
            )
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print("{}: {} finished!".format(time.ctime(), self.getName()))


# Consumer thread
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for _i in range(5):
            val = self.data.get()
            print(
                "%s: %s is consuming. %d in the queue is consumed!"
                % (time.ctime(), self.getName(), val)
            )
            time.sleep(random.randrange(10))
        print("{}: {} finished!".format(time.ctime(), self.getName()))


# Main thread
def main():
    queue = Queue()
    producer = Producer("Pro.", queue)
    consumer = Consumer("Con.", queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("All threads terminate!")


if __name__ == "__main__":
    main()
