# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import math

path = os.path.dirname(os.path.realpath(__file__))

pto_o = [[85, 167], [402, 219], [394, 527], [41, 506]]    # Puntos originales del cuadro Rosa
relacion = 3.5   # 350px / 100mm


def transformacion(image, img):
    h, w = img.shape[:2] 
    pto = np.float32([[pto_o[0]], [pto_o[1]], [pto_o[2]], [pto_o[3]]])
    print(pto)
    pto_t = np.float32([[0,0], [350, 0], [350,350], [0, 350]]) # 350px son 100mm
    M = cv2.getPerspectiveTransform(pto, pto_t)
    final = cv2.warpPerspective(img, M, (w,h))
    return final


def calculo_rect (img_f, pts_f, str_f):
    img_f = cv2.line(img_f, pts_f[0], pts_f[1], (0,0,255), 3) # Linea Horizontal
    img_f = cv2.line(img_f, pts_f[1], pts_f[2], (0,0,255), 3) # Linea Vertical
    dx = (pts_f[1][0] - pts_f[0][0]) / relacion
    dy = (pts_f[2][1] - pts_f[1][1]) / relacion
    img_f = cv2.putText(img_f , str_f, (100, 550), cv2.FONT_HERSHEY_PLAIN, 3.5, (0, 0, 0), 3)
    img_f = cv2.putText(img_f , str(round(dx,2)) + ' mm x ' + str(round(dy, 2)) + " mm", (50, 600), cv2.FONT_HERSHEY_PLAIN, 2.8, (0, 0, 0), 3)
    return img_f

def calculo_circ (img_f, centro_f, radio, str_f):
    img_f = cv2.line(img_f, radio[0], radio[1], (255,0,0), 3) # Radio
    radio = radio[0][0] - radio[1][0]
    img_f = cv2.circle(img_f, centro_f , radio,(0, 0,255),2) # Circunferencia
    r = (radio) / relacion
    circ = (math.pi * radio * 2) / relacion
    img_f = cv2.putText(img_f , str_f, (100, 550), cv2.FONT_HERSHEY_PLAIN, 3.5, (0, 0, 0), 3)
    img_f = cv2.putText(img_f , "Radio: " + str(round(r,2)) + ' mm - Circ: ' + str(round(circ, 2)) + " mm", (40, 600), cv2.FONT_HERSHEY_PLAIN, 1.9, (0, 0, 0), 3)
    return img_f



img = cv2.imread( path + '/original.png', 1)  
img_plant = np.zeros((img.shape[0], img.shape[1], 3), np.uint8) # Crea la plantilla para la imagen rectificada

img_aux = img.copy()
img_aux = cv2.putText( img_aux , 'Presione para medir-> 1:Tarjeta, 2:Goma, 3:Peso, 4: 50c', (25, 125), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 0), 2)

while(1):

    cv2.imshow('Seleccionar que quiero medir', img_aux)
    k = cv2.waitKey(0) & 0xFF
    img_transf = transformacion(img_plant, img)
    if k == ord('1'):

        pts_1 = ((380, 30), (575, 30), (575, 330), (380, 330))
        
        img_res = calculo_rect (img_transf, pts_1, "Tarjeta")

    if k == ord('2'):

        pts_1 = ((64, 413), (264, 413), (264, 482), (64, 482))

        img_res = calculo_rect (img_transf, pts_1, "Goma")

    if k == ord('3'):

        centro_pts_3 = (353,425)
        radio_3 = ((353,425), (313,425))

        img_res = calculo_circ (img_transf, centro_pts_3, radio_3, "Peso")

    if k == ord('4'):

        centro_pts_4 = (447,423)
        radio_4 = ((447,423), (402,423))

        img_res = calculo_circ (img_transf, centro_pts_4, radio_4, "50 Centavos")

    elif k == ord('q'):
        break

    cv2.imwrite( path + '/result.jpg', img_res)
    cv2.imshow('Resultado', img_res) 

cv2.waitKey(0)      
cv2.destroyAllWindows()


