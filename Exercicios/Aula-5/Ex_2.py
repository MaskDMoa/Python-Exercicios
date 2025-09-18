import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfPaises["Region"] = dfPaises["Region"].str.strip()

log = dfPaises['Population'].max()

log2 = dfPaises.loc[dfPaises['Population'] == log, ['Country', 'Region']]

print("O país que tem a maior População: ")

print(log2)