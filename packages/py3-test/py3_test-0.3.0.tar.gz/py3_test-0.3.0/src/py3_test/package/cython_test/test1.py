# Created on: 2018/2/24 10:36
# Email: lijicong@163.com
# desc
# import pyximport
# pyximport.install(pyximport=True)

from src.package.cython_test import helloworld

print(helloworld.print_test1("hello world"))
print(helloworld.print_test2("hello world"))
print(helloworld.print_test3(11111))
print(helloworld.print_dict({"a": "b"}))
