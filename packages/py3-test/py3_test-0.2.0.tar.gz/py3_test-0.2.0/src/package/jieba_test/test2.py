"""
@Time   : 2019/3/21
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import re

import requests

bset = set()
with open("test.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        data = {"analyzer": "max_analyzer", "text": line}
        r = requests.post("http://10.10.20.165:9200/decoration/_analyze", json=data)
        tokens = r.json()["tokens"]
        tmp_set = {adict["token"] for adict in tokens}
        bset.update(tmp_set)

with open("test2.txt", "w", encoding="utf-8") as f:
    for element in bset:
        if (
            len(element) > 1
            and len(element) < 4
            and bool(re.search("[a-zA-Z]", element)) is False
        ):
            f.write(element + "\n")
