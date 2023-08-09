"""
Created on 2015/12/13
@author: lijc210@163.com

"""
import re

import jieba

aset = set()
with open("test.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        aset.update(jieba.cut(line))

with open("test1.txt", "w", encoding="utf-8") as f:
    for element in aset:
        if (
            len(element) > 1
            and len(element) < 4
            and bool(re.search("[a-zA-Z]", element)) is False
        ):
            f.write(element + "\n")
