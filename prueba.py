from orderlib import *
import numpy as np



#A = np.random.randint(0,5,33)
#A = np.random.random(5)
A = [1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4, 1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4]
print(A)
quicksortThreeWay(A, 0, len(A) - 1)
print(A)