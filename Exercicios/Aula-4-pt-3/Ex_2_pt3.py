import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

gastos = dataset[1:, -2].astype(float) 

cond = gastos > 0

total = np.sum(gastos[cond])

print("A media de dinheiro gasto em missões com valores diponiveis e de {} ".format((total/cond.size)))