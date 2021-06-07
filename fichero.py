# Otra manera alternativa de buscar la infomración más eficiente
# podría ser sumar las líneas en las que aparece la expresión
# regular
fichero = open("data/covid_approval_polls.csv", 'r')
count1 = sum(1 for line in fichero if re.search('Huffington Post', line))
print("\nThe pattern Huffington_Post appears {} times".format(count1))