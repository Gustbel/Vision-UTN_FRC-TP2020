#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: practica_lista.py
# @authors: Jeremias Baez Carballo
#           Gustavo Bruno
#

import numpy as np

def opcion1(matriz):
    print(matriz[2])

def opcion2(matriz):
    for i in range(4):
        for j in range(4):
            if i == j:
                matriz[i][j] = 0        
    print(np.matrix(matriz))

def opcion3(matriz):
    acum=0
    for i in range(4):
        for j in range(4):
            acum = acum + matriz[i][j]
    print("El total de la suma de los elementos es: ", acum)

def opcion4(matriz):
    for i in range(4):
        for j in range(4):
            if (matriz[i][j] % 2) == 0:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    print(np.matrix(matriz))

try : 
    while True:
        matriz = [ [2,2,5,6], [0,3,7,4], [8,8,5,2], [1,5,6,1] ]
        print(np.matrix(matriz))
        print("\n\n Ingrese lo que desea realizar:\n 1- Seleccionar subarray [8,8,5,2]\n 2- Poner diagonal de la matriz en cero\n 3- Sumar todos los elementos del array\n 4- Setear valores pares en 0 y valores impares en 1\n")
        opcion = int(input())
        if opcion == 1:
            opcion1(matriz)
        elif opcion == 2:
            opcion2(matriz)
        elif opcion == 3:
            opcion3(matriz)
        elif opcion == 4:
            opcion4(matriz)
        input("Presionar una tecla para continuar con otra opcion, Ctr+c para salir del programa")
except KeyboardInterrupt:
        print("Saliendo del programa")


