#!/usr/bin/env python
# coding: utf-8

import cv2

# モザイク処理
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# モザイク処理をする範囲を設定
def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

# Haar Cascadeの識別器を読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 画像の読み込み
img = cv2.imread('image/Lenna.png')
# グレースケール化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 識別器による顔の検出
faces = face_cascade.detectMultiScale(gray)

# mosaic_area関数の呼び出し
for x, y, w, h in faces:
    dst_face = mosaic_area(img, x, y, w, h)

cv2.imshow("mosaic", dst_face)
cv2.imwrite('image/Lenna_mosaic.png', dst_face)

# リリース
cv2.waitKey(0)
cv2.destroyAllWindows()