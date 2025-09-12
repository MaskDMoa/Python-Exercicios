import numpy as np

dataset = np.loadtxt(r"C:\Users\BigHi\Desktop\Python\Exercicios\Aula-4-pt-3\space.csv", delimiter=';', dtype=str, encoding='utf-8')

empresas = dataset[1:, 1]

print(empresas)