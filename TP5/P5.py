#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import cv2
import numpy as np
import math 

path='/media/gustavo/DATOS/Facu/6to/Vision/Practicos/Practico5'

# Definimos Matrix M
angle = 30
tx = 700
ty = -14
M = np.float32([[math.cos(angle),math.sin(angle),tx],[-math.sin(angle), math.cos(angle),ty]])

img = cv2.imread(path + '/leon.png')    #Carga Imagen

#       PUNTO A

(h , w) = (img.shape[0], img.shape[1])

dst = cv2.warpAffine(img, M, (w,h))

cv2.imwrite(path + '/resultado_a.png' , dst)


#       PUNTO B

drawing = False # true if mouse is pressed

ix = -1
iy = -1
fx = 0
fy = 0
entro = False

def draw_rectangle (event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, entro
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix , iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True :
            cv2.rectangle(img, (ix,iy), (x ,y) , (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0 , 255 , 0), -1)
        fx, fy = x, y
        entro = True

img = cv2.imread(path + '/leon.png')    
img_orig = cv2.imread(path + '/leon.png')  #Cargamos dos veces porque la variable img se modificará

cv2.namedWindow ( ' image ' )
cv2.setMouseCallback(' image ', draw_rectangle)


while ( 1 ):           # Sostiene la imagen 
    cv2.imshow( ' image ' , img )
    if entro == True:
        img = img_orig[iy: fy, ix: fx]    # Corta la imagen
        
    k = cv2.waitKey ( 1 ) &0xFF
    if k == ord( 'q' ) :
        mode = not mode         #Finaliza
    if k == ord( 's' ) :
        img = cv2.warpAffine(img, M, (w,h))
        cv2.imwrite(path + '/resultado_b.png' , img)
        cv2.imshow( ' Resultado ' , img )


    
cv2.destroyAllWindows()