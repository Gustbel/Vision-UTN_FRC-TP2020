#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#mouse callback
def mouseCirc(event, x, y, flags, param):
    if event == cv2.EVENT_MBUTTONDBLCLK:
        print("cv2.EVENT_MBUTTONDBLCLK", event)
        cv2.circle(img, (x,y), 3, (255,0,0), -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("cv2.EVENT_LBUTTONDOWN", event)
        cv2.circle(img, (x,y), 3, (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        print("cv2.EVENT_LBUTTONUP", event)
        cv2.circle(img, (x,y), 3, (0,0,255), -1)

img = np.ones((512,512,3), np.uint8)*255
cv2.namedWindow("prueba")
cv2.setMouseCallback("prueba", mouseCirc)

while(True):
    cv2.imshow("prueba", img)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()