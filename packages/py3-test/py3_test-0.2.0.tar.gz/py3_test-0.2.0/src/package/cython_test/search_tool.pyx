# coding: utf-8
"""
@author: lijc210@163.com
@file: search_tool.py
@time: 2020/04/30
@desc: 功能描述。
"""
from collections import Counter, defaultdict

res_dict = defaultdict(float)


cpdef search_tool(list alist):
    cdef str k
    cdef float v
    cdef dict tmp_dict
    for tmp_dict in alist:
        for k, v in tmp_dict.items():
            res_dict[k] += v
    all_counter = Counter(res_dict)
    return all_counter
