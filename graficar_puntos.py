#
# Descripción: Programa que dibuja puntos en el plano y su mejor ajuste
#     	       a un polinomio de orden cuadrático
#
# Autor: Guillermo Palma 
#
# Email: gvpalma@usb.ve
# Versión: 0.1

import matplotlib.pyplot as plt
import math
import numpy as np

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
