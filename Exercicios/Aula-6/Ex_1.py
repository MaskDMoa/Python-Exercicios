import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfPaises['Region'] = dfPaises['Region'].str.strip()

df_norte = dfPaises[dfPaises['Region'] == 'NORTHERN AMERICA']

deathrate = df_norte['Deathrate']
birthrate = df_norte['Birthrate']
countries = df_norte['Country']

plt.xlabel('Países')
plt.ylabel('Taxas')

plt.plot(countries, deathrate, 'r-', countries, birthrate, 'b--')

plt.show()