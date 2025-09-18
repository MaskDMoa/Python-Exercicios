import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfPaises["Region"] = dfPaises["Region"].str.strip()

group_region = dfPaises.groupby('Region')

media = (group_region['Literacy (%)'].mean().reset_index().rename(columns = {'Literacy (%)' : 'Literacy_Media'}))

print(media)