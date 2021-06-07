# Importo las librerías para extraer los datos
from data_extr import datapollster

pollster = datapollster("data/pollster_ratings.xlsx")


# Creo una función que va a calcular el número de encuentas
# según el grado que poseen
def pollnumber(datafile):
    # Elaboro un diccionario ya que las calificaciones
    # deben modificarse según la información del ejercicio
    new_data = {"A+": "A", "A-": "A",
                "B+": "B", "B-": "B", "C+": "C", "D+": "D",
                "C-": "C", "D-": "D",
                "A/B": "B", "B/C": "C",
                "C/D": "D"}

    # combino esta diccionario y modifico en los datos
    pollstergrad = datafile.replace({'538 Grade': new_data})
    # elaboro el gráfico y hago que la función devuelva el número sefún
    # grado de las entrevistas realizadas
    pollstergrad.groupby("538 Grade")["Pollster"].count().plot(kind='bar')
    return pollstergrad.groupby("538 Grade")["Pollster"].count().iloc[0], \
           pollstergrad.groupby("538 Grade")["Pollster"].count().iloc[1], \
           pollstergrad.groupby("538 Grade")["Pollster"].count().iloc[2], \
           pollstergrad.groupby("538 Grade")["Pollster"].count().iloc[3]


A, B, C, D = pollnumber(pollster)

print("\nThe number of polls with A grade is {} \n".format(A))
print("\nThe number of polls with B grade is {} \n".format(B))
print("\nThe number of polls with C grade is {} \n".format(C))
print("\nThe number of polls with D grade is {} \n".format(D))