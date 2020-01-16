#!/usr/bin/env python
# coding: utf-8

import cv2

# Haar Cascadeの識別器を読み込み
face_cascade = cv2.CascadeClassifier('/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')

# 画像の読み込み
img = cv2.imread('image/Lenna.png')
# グレースケール化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 識別器を用いてグレースケール化された画像から顔を検出する
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# バウンディングボックス（顔）の描画
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # Haar Cascadeを用いて目を検出する
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # バウンディングボックス（目）の描画
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
        
# 画像の描画
cv2.imshow('img', img)

# リリース
cv2.waitKey(0)
cv2.destroyAllWindows()

