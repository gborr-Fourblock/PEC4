# import las librerías necesarias para el código y para
# extraer la información
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from data_extr import dataconcern, dataapproval, datapollster

pollster = datapollster("data/pollster_ratings.xlsx")
concern_polls = dataconcern("data/covid_concern_polls.csv")
approval_polls = dataapproval("data/covid_approval_polls.csv")
concern_polls2 = concern_polls[concern_polls.text.str.contains('coronavirus', case=False)]
approval_polls2 = approval_polls[approval_polls['text'].str.contains('Trump', case=False)]


# Creo un diccionario con el que modifico los grados para
# unificarlos
new_data = {"A+": "A", "A-": "A",
            "B+": "B", "B-": "B", "C+": "C", "D+": "D",
            "C-": "C", "D-": "D",
            "A/B": "B", "B/C": "C",
            "C/D": "D"}

# lo combino con el dataframe y sustituyo los grados
pollster = pollster.replace({'538 Grade': new_data})

# Vuelvo a crear un diccionario para asignar un número
# a cada letra
numerar = {"A": "1", "B": "0.5",
           "C": "0", "D": "-0.5", "F": "-1"}

# vuelvo a reemplazar con el diccionario
pollster = pollster.replace({'538 Grade': numerar})
# asigno un valor numérico a las columnas que van a ser sumadas
# para calcular el valor "credibilidad"
pollster['Predictive    Plus-Minus'] = pd.to_numeric(pollster['Predictive    Plus-Minus'])
pollster['538 Grade'] = pd.to_numeric(pollster['538 Grade'])
# sumo los datos de las dos columnas y creo la columna "credibilidad"
pollster['credibilidad'] = pollster.apply(lambda x: x['538 Grade'] + x['Predictive    Plus-Minus'], axis=1)

# Extraigo únicamente los datos de los entrevistadores con una
# credibilidad superior a 1.5
pollster1 = pollster.loc[(pollster['credibilidad'] >= 1.5)]

# Hago una lista con los datos de los entrevistadores
listas = pollster1['Pollster'].to_list()


# Creo una función que va a extraer la información de los entrevistadores
# con credibilidad superior a 1.5 
def concernsafterbefore(datafile):
  concern_polls2 = datafile.loc[datafile['pollster'].isin(listas)]
  despues = concern_polls2[concern_polls2['end_date']>'2020-09-01']
  antes = concern_polls2[concern_polls2['end_date']<='2020-09-01']

  fig = matplotlib.pyplot.gcf()
  fig.set_size_inches(50, 50)
  fig, (ax, ax2) = plt.subplots(ncols=2, sharey=True, sharex=True)
  for i in ax.patches:
      totals.append(i.get_width())
  antes[['very','somewhat',"not_very", "not_at_all"]].sum().plot(kind='barh', title = 'Concerns before Covid', ax=ax, figsize=(10,7),
                                                  color="indigo", fontsize=13)
  despues[['very','somewhat',"not_very", "not_at_all"]].sum().plot(kind='barh', title = "Concerns after Covid", ax=ax2, color="red")

  plt.show()
  return antes[['very', 'somewhat', "not_very", "not_at_all"]].sum(), despues[['very', 'somewhat', "not_very", "not_at_all"]].sum()


fig = px.bar(pollster1, x="Pollster", y="credibilidad", color_discrete_sequence=['crimson'], title="Entrevistadores con credibilidad superior o igual a 1.5")
fig.show()

antes, despues = concernsafterbefore(concern_polls2)
print("\nThe number of people not at all concerned before Covid is {} \n".format(int(antes.iloc[0])))
print("\nThe number of people not very concerned before Covid is {} \n".format(int(antes.iloc[1])))
print("\nThe number of people somewhat concerned before Covid is {} \n".format(int(antes.iloc[2])))
print("\nThe number of people very concerned before Covid is {} \n".format(int(antes.iloc[3])))

print("\nThe number of people not at all concerned after Covid is {} \n".format(int(despues.iloc[0])))
print("\nThe number of people not very concerned after Covid is {} \n".format(int(despues.iloc[1])))
print("\nThe number of people somewhat concerned after Covid is {} \n".format(int(despues.iloc[2])))
print("\nThe number of people very concerned after Covid is {} \n".format(int(despues.iloc[3])))
