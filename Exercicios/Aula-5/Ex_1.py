import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

#Letra A

dfPaises['Region'] = dfPaises['Region'].str.strip()

log = dfPaises.loc[dfPaises['Region'] == 'OCEANIA', ["Country"]]

print(log)

#Letra B

print("A quantidade de Paises na Oceania é de {}".format((dfPaises['Region'] == 'OCEANIA').sum()))

