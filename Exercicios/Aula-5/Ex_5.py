import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

def classificar(Death):
    if Death < 9:
        return 'Balanced'
    else:
        return 'Urgent'

dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(classificar)

print(dfPaises)
