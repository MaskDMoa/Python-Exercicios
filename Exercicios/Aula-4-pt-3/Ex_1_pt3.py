import numpy as np


dataset = np.loadtxt('space.csv', delimiter=',', dtype=str, encoding='utf-8')

status = dataset[1:,-1]

sucessos = np.sum(status == "Success")
falhas = np.sum(status == "Failure")

total = sucessos + falhas

print("A porceteagem de missões que deram certo foi de {}%".format(((sucessos * 100)/total))) 