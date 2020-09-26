#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

blue=(255,0,0)
red=(0,255,0)
green=(0,0,255)

img = np.zeros((512,512,3),np.uint8)
img = cv.line(img, (0,0), (500,500), blue, 3)
img = cv.ellipse(img, (255,255), (100,50), 0, 0, 180, 255, -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
img = cv.polylines(img,pts,True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "JereTEst", (10,500), font, 4, (255,255,255), 2, cv.LINE_AA)

cv.imshow(' frame ', img)
key = cv.waitKey(0)
print(key)
cv.destroyAllWindows()