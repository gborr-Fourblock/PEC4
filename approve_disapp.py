# Importo las librerías necesarias para ejecutar el código
# y las funciones de extracción de los datasets que voy a usar
import warnings
warnings.filterwarnings("ignore")
from data_extr import dataconcern, dataapproval, datapollster

# Ejecuto el código y extraigo las funciones con lo requerido en el ejercicio
pollster = datapollster("data/pollster_ratings.xlsx")
concern_polls = dataconcern("data/covid_concern_polls.csv")
approval_polls = dataapproval("data/covid_approval_polls.csv")

concern_polls2 = concern_polls[concern_polls.text.str.contains('coronavirus', case=False)]
approval_polls2 = approval_polls[approval_polls['text'].str.contains('Trump', case=False)]

# Creo una función para realizar el gráfico de barras que muestre la aprobación o desaprobación
# con las políticas Covid de Trump
def graf_appr(datafile):
    datafile.groupby("party")["approve", "disapprove"].sum().plot(kind='bar',
                                                                  title="Approval or disapproval of Trump's Covid policies")
    return datafile.groupby("party")["approve", "disapprove"].sum()

# Ejecuto la función e imprimo el resultado global y de cada uno
# de los datos
appdis = graf_appr(approval_polls2)

print(appdis)

print("\n {} people of the Democrat party approve Trump's Covid policy\n".format(int(appdis.iloc[0, 0])))
print("\n {} people of the Independent party approve Trump's Covid policy\n".format(int(appdis.iloc[1, 0])))
print("\n {} people of the Republican party approve Trump's Covid policy\n".format(int(appdis.iloc[2, 0])))
print("\n {} people of all parties that approve Trump's Covid policy\n".format(int(appdis.iloc[3, 0])))
print("\n {} people of the Democrat party disapprove Trump's Covid policy\n".format(int(appdis.iloc[0, 1])))
print("\n {} people of the Independent party disapprove Trump's Covid policy\n".format(int(appdis.iloc[1, 1])))
print("\n {} people of the Republican party disapprove Trump's Covid policy\n".format(int(appdis.iloc[2, 1])))
print("\n {} people of all  parties that disapprove Trump's Covid policy\n".format(int(appdis.iloc[3, 1])))