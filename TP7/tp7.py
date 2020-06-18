#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: tp7.py
# @authors: Gustavo Bruno
#           Jeremias Baez Carballo
#

import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
cPoint = 1

def seleccionPuntos(event, x, y, flags, param):
    global cPoint, p1, p2, p3, img1
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse button pressed")
        if cPoint == 1:
            p1 = x, y
            cv2.circle(img1, p1, 3, (255, 0, 0), 2)
        elif cPoint == 2:
            p2 = x, y
            cv2.circle(img1, p2, 3, (0, 255, 0), 2)
        elif cPoint == 3:
            p3 = x, y
            cv2.circle(img1, p3, 3, (0, 0, 255), 2)
        cPoint += 1
        cv2.imshow("imagen1", img1)

def tafin(imagen, s1h, s1w):
    source = np.array([(0, imagen.shape[0]), (0, 0), (imagen.shape[1], 0)], dtype=np.float32)
    destination = np.array([p1, p2, p3], dtype=np.float32)
    matrix = cv2.getAffineTransform(source, destination)
    mask = np.zeros((s1h, s1w, 3), np.uint8)
    mask[:] = (255, 255, 255)
    res = mask * cv2.warpAffine(imagen, matrix, (s1w, s1h))
    return res

try:
    img1 = cv2.imread(path+"/img/1.jpg", cv2.IMREAD_COLOR)
    original = img1.copy()
    cv2.namedWindow("imagen1")
    cv2.setMouseCallback("imagen1", seleccionPuntos)
    img2 = cv2.imread(path+"/img/2.jpeg", cv2.IMREAD_COLOR)
    # cv2.namedWindow("imagen2")
    print("Seleccione 3 puntos en orden de sentido horario para incrustar 1 en 2, presione a cuando\
        termine para mostrar el mariachi. Para volver a seleccionar los puntos para la transformacion\
            presione la letra R")
    xySize = img1.shape
    print("Size: ", xySize)
    while(True):
        cv2.imshow("imagen1", img1)
        # cv2.imshow("imagen2", img2)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("a"):
            print("Guardando la imagen salida.png")
            result = tafin(img2, img1.shape[0], img1.shape[1])
            # salida = cv2.addWeighted(img1, 0.5, result, 0.5, 0)
            resultGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(resultGray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            fondo = cv2.bitwise_and(img1, img1, mask=mask_inv)
            salida = cv2.add(fondo, result)
            cv2.imwrite(path+"/img/salida.png", salida)
            cv2.namedWindow("salida")
            cv2.imshow("salida", salida)
        elif key == ord("r"):
            print("Restaurando imagen, habilitando nueva seleccion")
            img1 = original.copy()
            cPoint = 1
            p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
            cv2.destroyWindow("salida")
        elif key == ord("q"):
            print("Saliendo del programa...\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion ejecutando el programa: %s", e)
    cv2.destroyAllWindows()