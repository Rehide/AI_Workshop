#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 画像の読み込み
img_org = cv2.imread('image/ball2.jpg')
# グレースケール化
imgray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
# メディアフィルターを用いて画像をぼかす
imgray = cv2.medianBlur(imgray, 5)

#　ハフ変換による円の検出
circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=750, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # 円の描画
    cv2.circle(img_org, (i[0],i[1]), i[2], (0,255,0), 2)
    # 中心点の描画
    cv2.circle(img_org, (i[0],i[1]), 2, (0,0,255), 3)

cv2.imshow('detected circles', img_org)
cv2.waitKey(0)
cv2.destroyAllWindows()