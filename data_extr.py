# Importo las librerías necesarias para el código de extracción
# de los dataset esto ayudará a facilitar la ejecución del resto
# de códigos
import pandas as pd


# Creo una función que limpie la información y extraiga la
# información sobre los encuestadores
def datapollster(datafile):
    pollsters = pd.ExcelFile(datafile)
    pollster = pd.read_excel(pollsters)
    pollster = pollster[pollster["Banned by 538"] == "no"]
    return pollster

pollster = datapollster("data/pollster_ratings.xlsx")


# Creo una función que limpie la información y extraiga el dataset sobre
# las preocupaciones de la población americana
def dataconcern(datafile):
    concern = open(datafile)
    concern_polls = pd.read_csv(concern)
    concern_polls = concern_polls[concern_polls["tracking"] == False]
    valores = pollster['Pollster'].to_list()
    concern_polls = concern_polls.loc[concern_polls['pollster'].isin(valores)]
    return concern_polls

concern_polls = dataconcern("data/covid_concern_polls.csv")


# Creo una función que limpie la información y extraiga el dataset sobre
# el acuerdo y desacuerdo con políticas Covid de la población americana
def dataapproval(datafile):
    approval = open(datafile)
    approval_polls = pd.read_csv(approval)
    approval_polls = approval_polls[approval_polls["tracking"] == False]
    valores = pollster['Pollster'].to_list()
    approval_polls = approval_polls.loc[approval_polls['pollster'].isin(valores)]
    return approval_polls

approval_polls = dataapproval("data/covid_approval_polls.csv")


