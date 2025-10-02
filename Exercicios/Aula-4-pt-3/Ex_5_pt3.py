import numpy as np

dataset = np.loadtxt("space.csv", delimiter=';', dtype=str, encoding='utf-8')

empresas = dataset[1:, 1]

print(empresas)