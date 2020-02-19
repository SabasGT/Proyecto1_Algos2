
import numpy as np
from orderlib import *
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice
from random import randrange

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

def algos(Arr:list):  # Funcion para ejecutar los algoritmos
    ArrCopy = list(Arr)

    # Corrida Mergesort
    mergeSort(Arr)

    Arr = list(ArrCopy)
    print("listo 1")

    # Corrida Quicksort Iterativo
    quicksortIter(Arr)  

    Arr = list(ArrCopy)
    print("listo 2")

    # Corrida Quicksort   
    quickSort(Arr, 0, len(Arr) - 1) 

    Arr = list(ArrCopy)
    print("listo 3")

    
    # Corrida Quicksort Median of 3    
    quicksortMedian(Arr, 0, len(Arr) - 1)    
    

    Arr = list(ArrCopy)
    print("listo 4")

    # Corrida Introsort
    introSort(Arr, 0, len(Arr) - 1)   

    Arr = list(ArrCopy)
    print("listo 5")

    """
    # Corrida Quicksort with 3-way-partitioning
    quicksortThreeWay(Arr, 0, len(Arr) - 1)  
    """

    Arr = list(ArrCopy)
    print("listo 6")

    # Corrida Dual Pivot Quicksort
    quicksortDual(Arr, 0, len(Arr) - 1)

    Arr = list(ArrCopy)
    print("listo 7")

    # Corrida Timsort
    sorted(Arr)

    print("listo 8")


#t = choice([1,2,3,4,5,6,7])
t = 1
n = 200

A = generadorArr(t,n)
print(A)
quicksortMedian(A,0,n - 1)