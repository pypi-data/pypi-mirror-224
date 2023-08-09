"""
@Time   : 2018/9/20
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import time
from concurrent.futures import ThreadPoolExecutor


def aaa(xxx=None):
    time.sleep(2)
    print(xxx)
    return xxx


EXECUTOR = ThreadPoolExecutor(max_workers=3)
all_task = [EXECUTOR.submit(aaa, xxx=x) for x in [1, 2, 3]]

# for future in as_completed(all_task):
#     data = future.result()
#     print("res", data)

for future in all_task:
    data = future.result()
    print("res", data)
