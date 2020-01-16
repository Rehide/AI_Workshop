#!/usr/bin/env python
# coding: utf-8

import cv2

cap = cv2.VideoCapture("../movie/car.mp4")# 動画の読み込み
# cap = cv2.VideoCapture(0) #  カメラ映像の読み込み


# 繰り返し処理（動画が終わる or 終了キーを押すまで）
while(True):
    # frame画像を読み込み
    ret, frame = cap.read() 
    
    # frame画像の表示
    cv2.imshow('frame', frame)
    
    # ESCを押すと終了
    if cv2.waitKey(1) == 27:
        break

#　動画のリリース
cap.release()
cv2.destroyAllWindows()

