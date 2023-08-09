"""
@author: lijc210@163.com
@file: test.py
@time: 2020/08/18
@desc: 功能描述。
"""
from ctypes import c_float, c_int, cdll

# 引入动态库libDemo.so
library = cdll.LoadLibrary("./libDemo.dll")
library.hello()
res = library.basicTest(c_int(10), c_float(12.34))
print(res)
