import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
from orderlib import *
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice
from random import randrange
from time import perf_counter
from math import sqrt
from statistics import mean, stdev

"""ARGPARSE"""

# Inicializar el argparse
tester = argparse.ArgumentParser(description='Script para comparar el tiempo de ejecucion de diversos algoritmos de ordenamiento')

# Añadir los argumentos para el programa
tester.add_argument('-i', help = "Numero de veces que se ejecutará la prueba", type = int)
tester.add_argument('-t', help = "Establece la prueba específica a ser llamada", type = int)
tester.add_argument('-g', help = "Activa la creacion de la grafica de resultados obtenidos", action = "store_true", default = False)
tester.add_argument('Enteros', metavar='N', type=int, nargs='+', help='Un numero de elementos para las pruebas') # Recibe la entrada posicional

# Procesamiento de los argumentos ingresados
args = tester.parse_args()

# Inicializacion por default de las 3 variables pertinentes a los parámetros de las pruebas
n = args.Enteros    #  Tamaño del arreglo
i = 3               #  Numero de pruebas
t = 1               #  Tipo de prueba

# Recibir los argumentos
if args.i:
    i = args.i

if args.t:
    t = args.t

if args.g:
    g = True
else:
    g = False

""" MANEJO DE ERRORES Y ENTRADAS INVALIDAS """   

# Manejo de Entrada de datos Incorrecta
try:
    assert(len(n) > 0 and int(i) > 0 and 1 <= int(t) <= 7)
except:
    print("Valores Invalidos. n e i deben ser mayor que 0 y t debe estar entre 1 y 7.")
    print("\nEl programa terminara.")
    tester.exit(status=0, message="\nERROR = Datos invalidos")

# Verificar que haya al menos dos cantidades de elementos N para graficar
if g:
    try:
        assert(len(n) >= 2)
    except:
        tester.exit(status=0, message="\nSi activa -g debe introducir al menos 2 cantidades de elementos a probar.")


""" BIENVENIDA """

# Mostrar en la terminal los valores registrados

print("i=" + str(i))
print("t=" + str(t))
print("g=" + str(g))


""" FUNCIONES """


def algos(Arr:list):  # Funcion para ejecutar los algoritmos
    ArrCopy = list(Arr)

    # Corrida Mergesort
    start = perf_counter() # Inicio tiempo de ejecucion
    mergeSort(Arr)
    end = perf_counter()   # Fin tiempo de ejecucion
    time_select = (end - start)
    mergesort.append(time_select)

    Arr = list(ArrCopy)

    # Corrida Quicksort Iterativo
    start = perf_counter()
    quicksortIter(Arr)
    end = perf_counter()
    time_select = (end - start)
    quick_iter.append(time_select)

    Arr = list(ArrCopy)

    # Corrida Quicksort
    start = perf_counter()
    quickSort(Arr, 0, len(Arr))
    end = perf_counter()
    time_select = (end - start)
    quick.append(time_select)

    Arr = list(ArrCopy)

    # Corrida Quicksort Median of 3
    start = perf_counter()
    quicksortMedian(Arr, 0, len(Arr) - 1)
    end = perf_counter()
    time_select = (end - start)
    quick_median.append(time_select)

    # Corrida Introsort
    start = perf_counter()
    introSort(Arr, 0, len(Arr) - 1)
    end = perf_counter()
    time_select = (end - start)
    intro.append(time_select)

    # Corrida Quicksort with 3-way-partitioning
    start = perf_counter()
    quicksortThreeWay(Arr, 0, len(Arr) - 1)
    end = perf_counter()
    time_select = (end - start)
    quick_way.append(time_select)

    # Corrida Dual Pivot Quicksort
    start = perf_counter()
    quicksortDual(Arr, 0, len(Arr) - 1)
    end = perf_counter()
    time_select = (end - start)
    quick_dual.append(time_select)

    # Corrida Timsort
    start = perf_counter()
    sorted(Arr)
    end = perf_counter()
    time_select = (end - start)
    tim.append(time_select)


def mostrar_resultados(size):  # Funcion para mostrar en pantalla los resultados de las pruebas acordes
    print("\nAnalisis para arreglo de " + str(n[size]) + " elementos.")

    print("\nTiempo de ejecucion promedio de Mergesort: " + str("{0:.2f}".format(mean(mergesort))) + "s." + 
          " STD: " + str("{0:.2f}".format(stdev(mergesort))) + "s." )
    promedios_merge.append(mean(mergesort))

    print("\nTiempo de ejecucion promedio de Quicksort Iterativo: " + str("{0:.2f}".format(mean(quick_iter))) + "s." +
          " STD: " + str("{0:.2f}".format(stdev(quick_iter))) + "s.")
    promedios_quickIter.append(mean(quick_iter))

    print("\nTiempo de ejecucion promedio de Quicksort: " + str("{0:.2f}".format(mean(quick))) + "s." + 
          " STD: " + str("{0:.2f}".format(stdev(quick))) + "s.")
    promedios_quick.append(mean(quick))

    print("\nTiempo de ejecucion promedio de Median-of-3 Quicksort: " + str("{0:.2f}".format(mean(quick_median))) + "s." +
          " STD: " + str("{0:.2f}".format(stdev(quick_median))) + "s.")  
    promedios_quickMedian.append(mean(quick_median))

    print("\nTiempo de ejecucion promedio de Introsort: " + str("{0:.2f}".format(mean(intro))) + "s." + 
          " STD: " + str("{0:.2f}".format(stdev(intro))) + "s." )
    promedios_intro.append(mean(intro))

    print("\nTiempo de ejecucion promedio de Quicksort con 3-way-partitioning: " + str("{0:.2f}".format(mean(quick_way))) + "s." +
          " STD: " + str("{0:.2f}".format(stdev(quick_way))) + "s.")
    promedios_quickWay.append(mean(quick_way))

    print("\nTiempo de ejecucion promedio de Dual Pivot Quicksort: " + str("{0:.2f}".format(mean(quick_dual))) + "s." + 
          " STD: " + str("{0:.2f}".format(stdev(quick_dual))) + "s.")
    promedios_quickDual.append(mean(quick_dual))

    print("\nTiempo de ejecucion promedio de Timsort: " + str("{0:.2f}".format(mean(tim))) + "s." +
          " STD: " + str("{0:.2f}".format(stdev(tim))) + "s.")  
    promedios_tim.append(mean(tim))


def mensaje_Inicial(t:int, size:int):  # Funcion para mostrar en pantalla una bienvenida y contexto al programa
    if t == 1:
        print("\nMostrando resultados de la prueba 1: Punto flotante para el arreglo de tamanyo " + str(n[size]) + ".")
        
    elif t == 2:
        print("\nMostrando resultados de la prueba 2: Ordenado para el arreglo de tamanyo " + str(n[size]) + ".")

    elif t == 3:
        print("\nMostrando resultados de la prueba 3: Ordenado Inverso para el arreglo de tamanyo " + str(n[size]) + ".")

    elif t == 4:
        print("\nMostrando resultados de la prueba 4: Cero-Uno para el arreglo de tamanyo " + str(n[size]) + ".")

    elif t == 5:
        print("\nMostrando resultados de la prueba 5: Mitad para el arreglo de tamanyo " + str(n[size]) + ".")

    elif t == 6:
        print("\nMostrando resultados de la prueba 6: Casi ordenado 1 para el arreglo de tamanyo " + str(n[size]) + ".")

    elif t == 7:
        print("\nMostrando resultados de la prueba 7: Casi ordenado 2 para el arreglo de tamanyo " + str(n[size]) + ".")


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


""" FUNCIONES GRAFICAS """
num_graficas = 0
marcadores = ['.', 'o', '*', '+', 'v', ',', '^', '<', '>', '1', '2', '3', '4', '5', '6', '7', '8', 's', 'p', 'P']
color_defecto = "C"
max_num_def_colores = 10

#
# Descripción: Encuentra el mejor ajuste de un conjunto de puntos
#              a un polinomio de orden cuadrático
#
# Parametros:
# x: Lista con las coordenadas del eje X.
# y: Lista con las coordenadas del eje Y.
#
def puntos_cuadraticos(x, y):
    fit = np.polyfit(x,y,2)
    fit_fn = np.poly1d(fit)
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = fit_fn(x_new)
    return x_new, y_new  

#
# Descripción: Dibuja puntos en el plano de la gráfica
#
# Parametros:
# x: Lista con las coordenadas del eje X.
# y: Lista con las coordenadas del eje Y.
# nombre: nombre de la grafica

def dibujar_grafica(x, y, nombre):
    global num_graficas
    global marcadores
    global color_defecto
    global max_num_def_colores
    marca = marcadores[num_graficas % len(marcadores)]
    color = color_defecto + str(num_graficas % max_num_def_colores)
    x_new, y_new = puntos_cuadraticos(x, y)
    plt.plot(x_new, y_new)
    plt.plot(x, y, color+marca, label=nombre)
    num_graficas += 1

#
# Descripción: Muestra en pantalla el gráfico dibujado
#
# Parametros:
# x_etiqueta: Etiqueta de las coordenadas del eje X.
# y_etiqueta: Etiqueta de las coordenadas del eje Y.
    
def mostrar_grafico(x_etiqueta, y_etiqueta):
    plt.xlabel(x_etiqueta)
    plt.ylabel(y_etiqueta)
    plt.legend(loc=2)
    plt.legend(bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
    plt.show()


def display_graph():  # Funcion para llamar al graficador
    dibujar_grafica(n, promedios_merge, "Mergesort")
    dibujar_grafica(n, promedios_quickIter, "Quicksort Iterativo")
    dibujar_grafica(n, promedios_quick, "Quicksort")
    dibujar_grafica(n, promedios_quickMedian, "Quicksort Median-of-3")
    dibujar_grafica(n, promedios_intro, "Introsort")
    dibujar_grafica(n, promedios_quickWay, "Quicksort with 3-way-partition")
    dibujar_grafica(n, promedios_tim, "Timsort")

    mostrar_grafico("Numero de elementos", "Tiempo(seg)")

""" COMIENZA EL PROGRAMA """

# Inicializar arreglos que almacenaran el tiempo promedio de corrida para cada N-corrida introducida en la linea de comandos.

promedios_merge = []
promedios_quickIter = []
promedios_quick = []
promedios_quickMedian = []
promedios_intro = []
promedios_quickWay = []
promedios_quickDual = []
promedios_tim = []

for size in range(len(n)):  # Ciclo para evaluar todos los elementos suministrados por el usuario

    mensaje_Inicial(t, size)

    # Inicializar arreglos para almacenar los tiempos de cada corrida en cada N distinto
    mergesort = []
    quick_iter = []
    quick = []
    quick_median = []
    intro = []
    quick_way = []
    quick_dual = []
    tim = []

    for k in range(i):  # Ciclo interno para realizar todas las pruebas i-veces
        arreglo = generadorArr(t, n[size])
        algos(arreglo)
    
    mostrar_resultados(size)

# Mostrar la grafica resultante en pantalla si -g fue llamado

if g:
    display_graph() 