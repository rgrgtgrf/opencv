import  cv2
import numpy as np
import math
"""
mad算法通过计算相对差的方法找到差值最小的子图
ncc算法是通过相关性计算的方式找到最接近1的算法
相关性公式是原图与模板每个位置的值和他们平均灰度值的差值的乘积之和除以他们平方差乘积的根
以下是我结合自己理解与网上资料做出的符合上述规则的函数
"""


def myncc(image1, image2):
    mean_image1 = sum(image1) / len(image1)
    mean_image2 = sum(image2) / len(image2)

    sum_cross = 0.0
    sum_sq_image1 = 0.0
    sum_sq_image2 = 0.0

    for val_image1, val_image2 in zip(image1, image2):
        val_image1_diff = val_image1 - mean_image1
        val_image2_diff = val_image2 - mean_image2
        sum_cross += val_image1_diff * val_image2_diff
        sum_sq_image1 += val_image1_diff ** 2
        sum_sq_image2 += val_image2_diff ** 2

    std_dev_image1 = math.sqrt(sum_sq_image1)
    std_dev_image2 = math.sqrt(sum_sq_image2)

    ncc = sum_cross / (std_dev_image1 * std_dev_image2)

    return ncc

image1 = cv2.imread("C:\\Users\\22170\\Desktop\\AAA.jpg")
image2 = cv2.imread("C:\\Users\\22170\\Desktop\\a1.jpg")
image5 = image1.copy()

res=myncc(image1,image2)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
top_left=min_loc
h,w=image2.shape[:2]
thishold=0.99
loc=np.where(res>=thishold)
for pt in zip(*loc[::-1]):
    bottom_right=(top_left[0]+w,top_left[1]+h)
    cv2.rectangle(image1,top_left,bottom_right,(0,0,255),2)

image4 = np.clip(1.2 * image2 + 35, 0, 255).astype(np.uint8)

image5[top_left[1]:top_left[1]+h, top_left[0]:top_left[0]+w] = image4

image3=cv2.resize(image1,(748,500))
image6=cv2.resize(image5,(748,500))

cv2.imshow('aaa',image3)
cv2.imshow('bbb',image6)
cv2.waitKey(0)