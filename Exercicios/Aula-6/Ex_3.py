import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfSpace = pd.read_csv('space.csv', delimiter=';')

dfRoscosmos = dfSpace[dfSpace['Company Name'] == 'Roscosmos']

failure = dfRoscosmos[dfRoscosmos['Status Mission'] == 'Failure']
success = dfRoscosmos[dfRoscosmos['Status Mission'] == 'Success']

qtfail = len(failure)
qtsuccess = len(success)

plt.pie(x=[qtsuccess, qtfail], labels=['% Missões com Sucesso','% Missões com Falhas'], autopct='%1.1f%%    ')
plt.show()