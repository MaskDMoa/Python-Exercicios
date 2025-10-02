import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfSpace = pd.read_csv('space.csv', delimiter=';')

usa = dfSpace[dfSpace['Location'].str.contains("USA")]['Company Name'].unique()
china = dfSpace[dfSpace['Location'].str.contains("China")]['Company Name'].unique()

qtd_usa = len(usa)
qtd_china = len(china)

plt.bar(['EUA', 'China'], [qtd_usa,qtd_china])

plt.show()