import numpy as np

arr1 = np.ones(8)

arr2 = np.random.randint(0, 9, 8)

arr3 = np.array(arr1 + arr2)

if arr3.sum() >= 40:
    print(arr3.reshape(2, 4))
else:
    print(arr3.reshape(4, 2))

