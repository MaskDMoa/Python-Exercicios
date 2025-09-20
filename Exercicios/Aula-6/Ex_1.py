import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dfPaises = pd.read_csv('paises.csv', delimiter=';')

deathrate = dfPaises['Deathrate']
birthrate = dfPaises['Deathrate']

plt.xlabel('')
plt.ylabel('')

plt.plot(deathrate)

plt.show()