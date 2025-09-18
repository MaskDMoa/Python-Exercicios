import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfPaises["Region"] = dfPaises["Region"].str.strip()

log = dfPaises.loc[dfPaises['Coastline (coast/area ratio)'] == 0, ['Country']]

log.to_csv('paises_v2.csv', sep=';')