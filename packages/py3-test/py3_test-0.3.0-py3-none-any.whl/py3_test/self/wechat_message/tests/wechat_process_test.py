# !/usr/bin/env python
import time
from multiprocessing import Process, freeze_support

from src.views.network_weixin2 import main

if __name__ == "__main__":
    freeze_support()
    p = Process(target=main)
    p.start()  # 让这个进程开始执行test函数里面的代码
    p.join()  # 等进程p结束之后，才会继续向下走
    while 1:
        time.sleep(2)
        print("aaaaaaaaa")
