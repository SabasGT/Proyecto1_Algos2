import numpy as np
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice

def generadorArr(t:int, n:int) -> list: # Funcionar para generar arreglos aletorios dependiendo del caso suministrado
    if t == 1:
        Arr = rand(n)
    elif t == 2:
        Arr = randint(0, n + 1, n)
    elif t == 3:
        Arr = sorted(rand(n))
    elif t == 4:
        Arr = sorted(randint(0, n + 1, n))
    elif t == 5:
        Arr = sorted(rand(n), reverse = True)
    elif t == 6:
        Arr = sorted(randint(0, n + 1, n), reverse = True)
    elif t == 7:
        Arr = choice([0, 1], size=(n))
    
    return Arr