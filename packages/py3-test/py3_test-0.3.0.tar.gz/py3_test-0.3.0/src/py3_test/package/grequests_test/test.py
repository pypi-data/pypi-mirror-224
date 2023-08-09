"""
@Time   : 2019/1/14
@author : lijc210@163.com
@Desc:  : 功能描述。
"""

import time

import grequests
import requests

urls = [
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
]


def method1():
    t1 = time.time()
    for url in urls:
        requests.get(url)
        # print res.status_code
    t2 = time.time()
    print("method1", t2 - t1)


def method2():
    tasks = [grequests.get(u) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=6)
    print(res)
    t2 = time.time()
    print("method2", t2 - t1)


if __name__ == "__main__":
    method1()
    method2()
