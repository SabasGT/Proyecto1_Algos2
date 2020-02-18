from orderlib import *
import numpy as np
from numpy.random import rand


t = 1
n = 20
A = rand(n)
print(A)
quickSort(A, 0, len(A))
print(A)

"""
#A = np.random.randint(0,5,33)
A = np.random.random(65000)
#A = [1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4, 1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4]
print(A)
quicksortDual(A, 0, len(A) - 1)
print(A)
"""