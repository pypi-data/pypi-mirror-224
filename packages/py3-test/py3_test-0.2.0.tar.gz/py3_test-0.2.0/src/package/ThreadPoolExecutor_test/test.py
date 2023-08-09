"""
@Time   : 2018/9/20
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import time
from concurrent.futures import ThreadPoolExecutor


def aaa(xxx=None, bbb=None):
    time.sleep(2)
    print(2)
    return "aaaaaaa"


EXECUTOR = ThreadPoolExecutor(max_workers=2)
res1 = EXECUTOR.submit(aaa, xxx="xxx", bbb="bbb")
res2 = EXECUTOR.submit(aaa, xxx="xxx", bbb="bbb")
res3 = EXECUTOR.submit(aaa, xxx="xxx", bbb="bbb")

print(res1.result())
print(res2.result())
print(res3.result())
