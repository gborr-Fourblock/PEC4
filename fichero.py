# Otra manera alternativa de buscar la infomración más eficiente
# podría ser sumar las líneas en las que aparece la expresión
# regular
import re
import pandas as pd
approval = open("data/covid_approval_polls.csv")
approval_polls = pd.read_csv(approval)
approval_polls = approval_polls.dropna(axis=0, subset=['start_date'])
fichero = open("data/covid_approval_polls.csv", 'r')
count1 = sum(1 for line in fichero if re.search('Huffington Post', line))
urls = approval_polls.url
regexp = r"^http[s]?://.*\.pdf"
count2 = sum(1 for approval in urls if re.match(regexp, approval) is not None)

# La diferencia entre el primer método y el segundo en el caso de url se debe
# a la eliminación de de los ficheros con campos vacíos en el dataframe
# ya que hay campos que tienen algunas columnas con campos vacíos pero sí
# tienen pdf con urls
print("\nThe pattern Huffington_Post appears {} times".format(count1))
print("\nThe pattern pattern url_pdf appears {} times".format(count2))
