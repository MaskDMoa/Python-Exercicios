import numpy as np

arr1 = np.arange(0, 51, 2)

arr2 = np.arange(100, 49, -2)

conc = np.sort(np.concatenate((arr1, arr2)))

print(conc)

