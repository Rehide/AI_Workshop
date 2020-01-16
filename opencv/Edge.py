#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('image/Lenna.png', 0)

# 画像のエッジ検出
edges = cv2.Canny(img,100, 200)

# 画像の保存
cv2.imwrite("image/Lenna_edge.png", edges)
# 画像の表示
cv2.imshow('edges', edges)

# 画像のリリース
cv2.waitKey(0)
cv2.destroyAllWindows()

