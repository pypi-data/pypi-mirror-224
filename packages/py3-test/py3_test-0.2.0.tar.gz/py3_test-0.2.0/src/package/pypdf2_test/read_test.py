"""
@author: lijc210@163.com
@file: 1.py
@time: 2020/03/26
@desc: 功能描述。
https://blog.csdn.net/xingxtao/article/details/79056341
"""

# encoding:utf-8
from PyPDF2 import PdfFileReader

readFile = "商家体检报告-上海-金令设计装潢.pdf"
# 获取 PdfFileReader 对象
pdfFileReader = PdfFileReader(
    readFile
)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
# 获取 PDF 文件的文档信息
documentInfo = pdfFileReader.getDocumentInfo()
print("documentInfo = %s" % documentInfo)
# 获取页面布局
pageLayout = pdfFileReader.getPageLayout()
print("pageLayout = %s " % pageLayout)

# 获取页模式
pageMode = pdfFileReader.getPageMode()
print("pageMode = %s" % pageMode)

xmpMetadata = pdfFileReader.getXmpMetadata()
print("xmpMetadata  = %s " % xmpMetadata)

# 获取 pdf 文件页数
pageCount = pdfFileReader.getNumPages()

print("pageCount = %s" % pageCount)
for index in range(0, pageCount):
    # 返回指定页编号的 pageObject
    pageObj = pdfFileReader.getPage(index)
    print(
        "index = %d , pageObj = %s" % (index, type(pageObj))
    )  # <class 'PyPDF2.pdf.PageObject'>
    # 获取 pageObject 在 PDF 文档中处于的页码
    pageNumber = pdfFileReader.getPageNumber(pageObj)
    print("pageNumber = %s " % pageNumber)
