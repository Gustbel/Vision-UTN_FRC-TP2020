#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: tp6.py
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
    global cPoint, p1, p2, p3, img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse button pressed")
        if cPoint == 1:
            p1 = x, y
            cv2.circle(img, p1, 3, (255, 0, 0), 2)
        elif cPoint == 2:
            p2 = x, y
            cv2.circle(img, p2, 3, (0, 255, 0), 2)
        elif cPoint == 3:
            p3 = x, y
            cv2.circle(img, p3, 3, (0, 0, 255), 2)
        cPoint += 1
        cv2.imshow("imagen", img)

def tafin(imagen, rHeight, rWidth):
    source = np.array([p1, p2, p3], dtype=np.float32)
    destination = np.array([(0, rHeight), (0, 0), (rWidth, 0)], dtype=np.float32)
    matrix = cv2.getAffineTransform(source, destination)
    res = cv2.warpAffine(imagen, matrix, (rWidth, rHeight))
    return res
try:
    img = cv2.imread(path+"/img/wildwest.jpg", cv2.IMREAD_COLOR)
    original = img.copy()
    cv2.namedWindow("imagen")
    cv2.setMouseCallback("imagen", seleccionPuntos)
    print("Seleccione 3 puntos en orden de sentido horario en la imagen y presione a para generar \
        la transformacion afin, r para restaurar la imagen y volver a seleccionar los puntos y q para\
         salir")
    xySize = img.shape
    print("Size: ", xySize)
    while(True):
        cv2.imshow("imagen", img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("a"):
            rH = int(input("Ingrese el alto de la imagen de salida que quiere generar\n"))
            rW = int(input("Ingrese el ancho de la imagen de salida que quiere generar\n"))
            print("Guardando la imagen resultado.png")
            result = tafin(img, rH, rW)
            cv2.imwrite(path+"/img/resultado.png", result)
            cv2.namedWindow("resultado")
            cv2.imshow("resultado", result)
        elif key == ord("r"):
            print("Restaurando imagen, habilitando nueva seleccion")
            img = original.copy()
            cPoint = 1
            p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
            cv2.destroyWindow("resultado")
        elif key == ord("q"):
            print("Saliendo del programa...\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion ejecutando el programa: %s", e)
    cv2.destroyAllWindows()