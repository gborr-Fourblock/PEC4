# Importo las librerías necesarias y las funciones de
# extracción de la información
import matplotlib.pyplot as plt
from data_extr import dataconcern, dataapproval, datapollster


# Extraigo los datos necesarios
pollster = datapollster("data/pollster_ratings.xlsx")
concern_polls = dataconcern("data/covid_concern_polls.csv")
approval_polls = dataapproval("data/covid_approval_polls.csv")
concern_polls2 = concern_polls[concern_polls.text.str.contains('coronavirus', case=False)]
approval_polls2 = approval_polls[approval_polls['text'].str.contains('Trump', case=False)]


# Con esta función calculo el número de personas entrevistadas y lo muestro
def sumsample(datafile):
    return datafile["sample_size"].sum()


print("\nThe total sample size of the population interviewed in polls is {} people \n".format(sumsample(concern_polls2)))


# Con esta función calculo las personas muy y para nada preocupadas por
# la economía, elaboro un gráfico y lo muestro en pantalla
def econconcern(datafile):
    suma1 = datafile.loc[datafile['subject'] == "concern-economy", 'very'].sum()
    suma2 = datafile.loc[datafile['subject'] == "concern-economy", 'not_at_all'].sum()
    estos = ["very concerned", "not_at_all concerned"]
    datos = [suma1, suma2]
    plt.bar(estos, datos)
    plt.title('Population concerned about the economy')
    plt.xlabel('Concerns about the economy')
    plt.ylabel('Population')
    plt.show()
    return suma1, suma2


very, not_very = econconcern(concern_polls2)

print("\nThe number of the population very concerned about the economy is {} \n".format(very))
print("\nThe number of the population not_at_all concerned about the economy is {} \n".format(not_very))


# Con esta función calculo el porcentaje de personas muy y para nada preocupadas por
# la infección, elaboro un gráfico y lo muestro en pantalla
def infeconcern(datafile):
    suma3 = datafile.loc[datafile['subject'] == "concern-infected", 'very'].sum()
    suma4 = datafile.loc[datafile['subject'] == "concern-infected", 'not_at_all'].sum()
    suma5 = datafile.loc[datafile['subject'] == "concern-infected", 'somewhat'].sum()
    suma6 = datafile.loc[datafile['subject'] == "concern-infected", 'not_very'].sum()

    porcentaje1 = suma3/(suma3+suma4+suma5+suma6)*100
    porcentaje2 = suma4/(suma3+suma4+suma5+suma6)*100

    estos1 = ["very concerned", "not_at_all concerned"]
    datos1 = [porcentaje1, porcentaje2]

    plt.bar(estos1, datos1)
    plt.title('Population concerned about the infection')
    plt.xlabel('Concerns about the infection')
    plt.ylabel('Population (in % of population interviewed)')
    plt.show()
    return "%.2f" % porcentaje1, "%.2f" % porcentaje2


veryinf, not_veryinf = infeconcern(concern_polls2)
print("\nThe percentage  of  population very concerned about the infection is {} \n".format(veryinf))
print("\nThe percentage of  population not_at_all concerned about the infection is {} \n".format(not_veryinf))
