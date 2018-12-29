#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np

#カメラのデバイス設定 映らないときはここをいじってみると良い
cap = cv2.VideoCapture(1)
#バッファ時間指定 遅延時間を調整することが可能
countMax = 150
#初期化
count = 0
#画面サイズの調整 各自で変更してください
w=1920
h=1080

#バッファの配列を用意
buf = np.empty([countMax,h,w,3],np.uint8)  #最大値は256

#初回読み込み
for i in range(countMax):
    ret, frame = cap.read()

    #動画サイズの変更
    frame2 = cv2.resize(frame,(w,h))

    #バッファに格納
    buf[i] = frame2
    print "read"

while(True):
    #再生
    cv2.imshow('camera caputure', buf[count])
    # スペースで閉じる 
    if cv2.waitKey(1) == 32:
        break  

    ## Capture frame-by-frame##
    #retは戻り値を表す
    #"ret"は,cap.read()でフレームが正しく読み込めたかどうかを教えてくれるフラグ
    ret, frame = cap.read()

    #動画サイズの変更
    frame2 = cv2.resize(frame,(w,h))

    #バッファに格納
    buf[count] = frame2

    #カウント
    count = count +1
    print count

    #バッファをリセット
    if count == countMax:
        count = 0


#キャプチャを解放
cap.release()
cv2.destroyAllWindows()