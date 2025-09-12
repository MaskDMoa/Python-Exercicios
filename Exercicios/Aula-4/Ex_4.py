import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

linhas, coluns = matriz.shape

tipo = ""

if (linhas * coluns) % 2 == 0:
    tipo = "par"
else:
    tipo = "ímpar"

print("A matriz pode virar um vetor unidimensional com número {} de elementos".format(tipo))