from orderlib import *
import numpy as np


#A = np.random.randint(0,4096,1000)
A = np.random.random(65536)
introSort(A, 0, len(A) - 1)
print(A)