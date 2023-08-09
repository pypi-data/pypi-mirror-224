"""
Created on 2017/10/26 0026 11:55
@author: lijc210@163.com
Desc:
"""

import re

pattern1 = re.compile(r".*\d+")
pattern2 = re.compile(r".*[a-zA-Z]+")

# with open("sensitive_word.txt","w") as fw:
#     with open('wordsfilter.txt','r') as f:
#         line_list = f.readlines()
#         for aline in line_list:
#             # if "." not in aline and len(aline) <= 12 and not pattern1.match(aline) and not pattern2.match(aline):
#             if "." not in aline and len(aline) <= 18 and not pattern1.match(aline):
#                 fw.write(aline.strip()+"\n")

with open("sensitive_word.txt") as f:
    line_list = f.readlines()
    for aline in line_list:
        if len(aline.strip()) <= 3:
            print(aline.strip())

# aset = set([])
# with open('sensitive_word.txt','r') as f:
#     line_list = f.readlines()
#     for line in line_list:
#         aset.add(line.strip())

# with open('sensitive_word.txt','w') as fw:
#     for key in aset:
#         fw.write(key+"\n")
