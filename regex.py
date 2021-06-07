# Importo las librerías necesarias para el código de extracción
import re

# Abro el fichero y separo los datos para que se pueda
# parsear la información del fichero
with open("data/covid_approval_polls.csv") as f:
    data = f.read().strip()


# Creo una función que extraiga las veces en las que se repitan
# los regex en el fichero
def app_times(regex_def, datafile):
    return len(re.findall(regex_def, datafile))


print("The pattern Huffington_Post appears {} times".format(app_times('Huffington Post', data)))
print("The pattern url_pdf appears {} times".format(app_times('^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])|.pdf', data)))



