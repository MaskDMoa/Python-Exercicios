import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

procura = dataset[1:, 1] 

cond = procura == "SpaceX"

gastos = dataset[1:, -2].astype(float) 

print("A missão mais cara do SpaceX foi de {}".format(np.max(gastos[cond])))

