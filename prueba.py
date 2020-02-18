from orderlib import *
import numpy as np

#A = [random.randint(0, 4096**2) for iter in range(4096)]
A = np.random.randint(0,4096,4096)
A = sorted(A)
print(A)
quicksortMedian(A, 0, len(A) - 1)
print(A)