"""
Created on 2017/9/30 0030 17:19
@author: lijc210@163.com
Desc:
"""

import cv2

if __name__ == "__main__":
    # show image with imshow
    img = cv2.imread("1.png", 1)
    print(img)
    # print(cv2.WINDOW_NORMAL)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# #导入cv模块
# import cv2 as cv
# #读取图像，支持 bmp、jpg、png、tiff 等常用格式
# img = cv.imread("C:\Users\Administrator\Desktop\1.png")
# #创建窗口并显示图像
# cv.namedWindow("Image")
# cv.imshow("Image",img)
# cv.waitKey(0)
# #释放窗口
# cv.destroyAllWindows()
