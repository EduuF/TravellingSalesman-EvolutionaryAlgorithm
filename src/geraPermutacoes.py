from confing import distancias, QUANTIDADE_INDIVIDUOS
import numpy as np
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html

def gera_permutacoes():
    arr = [[j for j in range(len(distancias))] for i in range(QUANTIDADE_INDIVIDUOS)]

    for i in arr:
        np.random.shuffle(i)
    return arr