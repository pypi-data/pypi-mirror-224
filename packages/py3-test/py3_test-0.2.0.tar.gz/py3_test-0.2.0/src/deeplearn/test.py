from detector import TextDetector

d = TextDetector("333.jpg")
boxes = d.detect()
# for box in boxes:
#     cv2.rectangle(d.resize_img, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 3)
# cv2.imwrite("222.jpg", d.resize_img)

# d = cv2.imread("111.jpg")
# print d
#
#
# from PIL import Image
# import numpy as np
# print np.array(Image.open("111.jpg"))
