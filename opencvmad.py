import  cv2

import numpy as np

"""

以下的mad是我自己在网上找的代码，mymad是根据我自己的理解以及csdn上博客的公式尝试做出来的,
但是时间复杂度只能为O(n的二次幂)，离散卷积没太看懂，以我的能力算法改进有点困难，再加上电脑轻薄本我怕它一直在那算就崩溃了，所以并没有运行出来结果,后面是用的网上方法框选目标图像
后面的custom_match方法也是源自网上

"""
def mad_fifter(img, threshold=3.5):
    """
    使用MAD算法进行异常点检测
    :param img: 输入图像，灰度图像
    :param threshold: 阈值系数，默认为3.5
    :return: 滤波后的图像
    """
    # 计算中位数和标准差
    median = np.median(img)
    abs_dev = np.abs(img - median)
    std = np.median(abs_dev) * 1.4826

    # 判断像素是否为异常点
    threshold_value = threshold * std
    mask = abs_dev > threshold_value
    img_filtered = img.copy()
    img_filtered[mask] = median

    return img_filtered

def mymad(image, template):
    image_h, image_w = image.shape[:2]
    template_h, template_w = template.shape[:2]
    min_diff = float('inf')
    loc = (0, 0)

    # 遍历搜索图像中的每个子图,如果遇到更为匹配的点就更新loc的值
    for i in range(image_h - template_h + 1):
        for j in range(image_w - template_w + 1):
            diff = np.abs(image[i:i+template_h, j:j+template_w] - template)
            mad = np.mean(diff)
            if mad < min_diff:
                min_diff = mad
                loc = (j, i)
    return loc
def custom_match(image, template):
    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 计算MAD
    mad_image = mad_fifter(gray_image)
    mad_template = mad_fifter(gray_template)

    # 计算匹配结果
    result = cv2.matchTemplate(mad_image, mad_template, cv2.TM_CCOEFF_NORMED)

    return result





image1 = cv2.imread("C:\\Users\\22170\\Desktop\\AAA.jpg")
image2 = cv2.imread("C:\\Users\\22170\\Desktop\\a1.jpg")
image5 = image1.copy()
#res=cv2.matchTemplate(image1,image2,cv2.TM_SQDIFF_NORMED)
#res=mymad(image1,image2)
res=custom_match(image1,image2)
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