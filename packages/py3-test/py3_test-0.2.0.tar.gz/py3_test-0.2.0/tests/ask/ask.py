"""
Created on 2017/8/28 0028
@author: lijc210@163.com
Desc: 功能描述。
"""

import csv

f = csv.reader(open("ask.txt"))
for line in f:
    for img_url in eval(line[1]):
        entity_type = "10"
        entity_id = line[0]
        img_height = "450"
        img_width = "600"
        print(
            entity_type
            + "\t"
            + entity_id
            + "\t"
            + img_url
            + "\t"
            + img_height
            + "\t"
            + img_width
        )
