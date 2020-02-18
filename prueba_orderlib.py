import argparse
import sys
import numpy as np
import graficar_puntos as gp
from orderlib import *
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice
from random import randrange
from time import perf_counter
from math import sqrt
from statistics import mean, stdev

def generadorArr(t:int, n:int) -> list: # Funciona para generar arreglos aletorios dependiendo del caso suministrado
    # t es un entero que indica cual prueba de la 1 a la 7 se va a realizar y n es el entero que señala el numero
    # de elementos que tendran de los arreglos generados.
    # assert(1 <= t <= 7 and n >= 0)

    def arreglo5(n:int):
        # Funcion que se encarga de generar el arreglo "Mitad"
        # n es el numero de elementos del arreglo.
        # assert(n >= 0)
        arreglo = [0]*n
        for i in range(n//2):
            arreglo[i] = i + 1
            arreglo[n - i - 1] = i + 1

        return arreglo

    
    def arreglo6(n:int):
        # Funcion que se encarga de generar el arreglo "Casi ordenado 1"
        # n es el numero de elementos del arreglo.
        # assert(n >= 0)
        ordenado = sorted(randint(0, n + 1, n))
        i = 0
        while i != 16:
            k = randrange(0, n - 8)
            ordenado[k], ordenado[k + 8] = ordenado[k + 8], ordenado[k]
            i += 1

        return ordenado

    
    def arreglo7(n:int):
        # Funcion que se encarga de generar el arreglo "Casi ordenado 2"
        # n es el numero de elementos del arreglo.
        # assert(n >= 0)
        ordenado = sorted(randint(0, n + 1, n))
        i = 0
        while i != (n//4):
            print(i)
            k = randrange(0, n - 4)
            ordenado[k], ordenado[k + 4] = ordenado[k + 4], ordenado[k]
            i += 1

        return ordenado


    if t == 1:
        Arr = rand(n)                                        # Punto Flotante
    elif t == 2:
        Arr = sorted(randint(0, n + 1, n))                   # Arreglo ordenado de enteros            
    elif t == 3:
        Arr = sorted(randint(0, n + 1, n), reverse = True)   # Arreglo ordenado a la inversa de enteros
    elif t == 4:
        Arr = choice([0, 1], size=(n))                       # Arreglo de 0 y 1
    elif t == 5:
        Arr = arreglo5(n)                                    # Arreglo de la forma (1, 2,..., N/2, N/2,...,2,1)
    elif t == 6:
        Arr = arreglo6(n)                                    # Arreglo casi ordenado 1
    elif t == 7:
        Arr = arreglo7(n)                                    # Arreglo casi ordenado 2
    
    return Arr


