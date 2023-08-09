"""
Created on 2017/10/31 0031 10:27
@author: lijc210@163.com
Desc:
"""

import re

aset = {
    ".",
    "-",
    ",",
    "'",
    '"',
    ":",
    "。",
    "\\",
    "&",
    "`",
    "~",
    "!",
    "@",
    "#",
    "%",
    "*",
    "(",
    ")",
    "=",
    "+",
    "_",
    "|",
    "?",
    "@",
    "",
    " ",
    " ",
    "\r",
    "\n",
    "-",
    "、",
    "—",
}
text = "aaa习**近- 平aaa"

pattern1 = re.compile("习")
pattern = re.compile('([\\.\\-,\\":。&`~!@#%\\*()=+_|?+\r\n、—/\\s]+)')

s = re.findall(pattern, text)
print(s)

# if s:
#     ss=s[0].replace('习','').replace('近','').replace('平','')
#     print ss
#     if set(ss)&aset==set(ss):
#         print('满足条件')
