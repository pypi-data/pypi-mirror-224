"""
@Time   : 2019/3/21
@author : lijc210@163.com
@Desc:  : 功能描述。
"""

aset = set()
with open("test1.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        aset.add(line)

bset = set()
with open("test2.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        bset.add(line)

with open("test3.txt", "w", encoding="utf-8") as f:
    for element in aset - bset:
        f.write(element + "\n")
