"""
@Time   : 2018/12/26
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
from queue import Queue

A_Q = Queue()
B_Q = Queue()
data = ["A", "B", "B", "A", "B", "B", "A"]

A_list = [x for x in data if x == "A"]
B_list = [x for x in data if x == "B"]

print(A_list)
print(B_list)

for i in A_list:
    A_Q.put(i)
for i in B_list:
    B_Q.put(i)

new_data = []
for x in data:
    if x == "A":
        new_data.append(A_Q.get())
    elif x == "B":
        new_data.append(B_Q.get())

print(new_data)
