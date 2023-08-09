"""
@Time   : 2018/9/20
@author : lijc210@163.com
@Desc:  : 测试是否释放
"""
import time
from concurrent.futures import ThreadPoolExecutor

from utils.logging_ import FileHandler_
from utils.run_log_time import run_time_log

logger_func = FileHandler_(
    getLogger="func",
    setLevel="logging.INFO",
    filename="test3.log",
    mode="w",
    StreamHandler=False,
    formatter=None,
)


@run_time_log(
    thr_time=0.3,
    logger=logger_func,
    message="",
    stop_time=4,
    stop_return=[],
    force_stop=True,
)
def aaa(xxx=None, yyy=None):
    time.sleep(2)
    print(xxx)
    return yyy


@run_time_log(
    thr_time=0.3,
    logger=logger_func,
    message="",
    stop_time=1,
    stop_return=[],
    force_stop=True,
)
def bbb(xxx=None, yyy=None):
    time.sleep(2)
    print(xxx)
    return yyy


EXECUTOR = ThreadPoolExecutor(max_workers=10)
for _x in range(20):
    res1 = EXECUTOR.submit(aaa, xxx="xxx", yyy="1")
    res2 = EXECUTOR.submit(bbb, xxx="xxx", yyy="2")

    print(res1.result())
    print(res2.result())

while 1:
    print("aaaa")
    time.sleep(1)
