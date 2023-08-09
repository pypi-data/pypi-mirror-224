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
    return xxx


with ThreadPoolExecutor(max_workers=5) as executor:
    executor.submit(aaa)

print("aaa")
