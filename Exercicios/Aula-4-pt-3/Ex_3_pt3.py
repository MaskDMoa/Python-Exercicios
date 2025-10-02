import numpy as np

dataset = np.loadtxt("space.csv", delimiter=';', dtype=str, encoding='utf-8')

missoes = np.sum(np.char.find(dataset[1:,2], "USA") >= 0)

print("O total de missões no EUA foram de {}".format(missoes))

