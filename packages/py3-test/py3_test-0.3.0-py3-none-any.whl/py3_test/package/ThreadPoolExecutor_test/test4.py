"""
@Time   : 2018/9/20
@author : lijc210@163.com
@Desc:  : 测试是否释放
"""
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Array, Process

num = Array("i", [1, 2, 3, 4, 5])  # 主进程与子进程共享这个数组


# @run_time_log(thr_time=0.3, logger=logger_func, message='', stop_time=4, stop_return=[], force_stop=True)
def aaa(xxx=None, yyy=None):
    time.sleep(2)
    print(xxx)
    return yyy


# @run_time_log(thr_time=0.3, logger=logger_func, message='', stop_time=1, stop_return=[], force_stop=True)
def bbb(xxx=None, yyy=None):
    print(num)
    time.sleep(2)
    print(xxx)
    return yyy


# while 1:
#     print("aaaa")
#     time.sleep(1)


def test():
    EXECUTOR = ThreadPoolExecutor(max_workers=10)
    res1 = EXECUTOR.submit(aaa, xxx="xxx", yyy="1")
    res2 = EXECUTOR.submit(bbb, xxx="xxx", yyy="2")

    print(res1.result(10))
    print(res2.result(0.1))


if __name__ == "__main__":
    p = Process(target=test)
    p.start()
    p2 = Process(target=test)
    p2.start()  # 让这个进程开始执行test函数里面的代码
    # 让这个进程开始执行test函数里面的代码
    p.join()
    p2.join()  # 等进程p结束之后，才会继续向下走
    print("---main----")
