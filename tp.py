import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import operator

all_months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
data = pd.read_excel('Climat.xlsx','SI ',usecols=range(3,15),skiprows=4,skipfooter=17,header=None)
data.columns = all_months


switcher = {
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Août",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Décembre"
}

worldData = pd.read_csv('city_temperature.csv', sep=',')
europeData = worldData.loc[worldData['Region'] == 'Europe']
europeData = europeData.drop(columns=['State', 'Region', 'Country'])
europeData = europeData.loc[europeData['AvgTemperature'] != -99.0]
europeData = europeData.loc[europeData['Year'] == 2018]
europeData['AvgTemperature'] = (europeData['AvgTemperature'] - 32) / 1.8


def correctData():
    for value in data :
        for i in range(len(data)) :
            if type(data[value][i])==str:
                data[value][i]=(data[value][i-1]+data[value][i+1])/2


def findAverage(month):
    moyenne = data[month]
    return moyenne.describe()


def createCurvesByMonth(month):
    plt.plot(data[month])
    plt.title('Graphique des variations de température du mois de '+month)
    plt.xlabel('Jours')
    plt.ylabel('Température (°C)')
    plt.show()
    plt.close()

def createCurvesAllMonth():
    for column in data:
        plt.plot(data[column].dropna())
        mplcursors.cursor(hover=True)
        plt.title('Graphique des variations de température du mois de ' + column)
        plt.xlabel('Jours')
        plt.ylabel('Température (°C)')
        plt.show()
    plt.close()

def createCurvesByYear():
    allValues = []
    for column in data :
        allValues = [*allValues, *data[column].dropna()]
    plt.plot(allValues)
    plt.title('Graphique des variations de température de l\'année')
    plt.xlabel('Jours')
    plt.ylabel('Température (°C)')
    plt.show()
    plt.close()

def findCapital():
    cityFound = ''
    sumDif = {}
    for city in europeData['City'].unique():
        dfTemp = europeData.loc[europeData['City'] == city]
        sumDifTemp = 0
        for month in dfTemp['Month'].unique():
            sumDifTemp += abs(float(dfTemp['AvgTemperature'].loc[dfTemp['Month'] == month].mean()) - float(data[switcher.get(month)].mean()))
        sumDif[city] = sumDifTemp

    maxDif = 1000
    for x in sumDif:
        if (sumDif[x] < maxDif):
            maxDif = sumDif[x]
            cityFound = x
    return sorted(sumDif.items(), key=operator.itemgetter(1,0))

def menu():
    while True:
        try:
            result = int(input("Que veux tu savoir: 1- Moyenne/écart_type/min/max  2- Diagramme 3- Capitale 4- Exit : " ))
        except ValueError:
            print("Error! This is not a number. Try again.")
        if (result == 1):
            month = input('Quelle est le mois souhaitez ?')
            print(findAverage(month))
        if (result == 2):
            menuYear()
        if (result == 3):
            print(findCapital())
        if (result == 4):
            break
# The function is called

def menuYear():   
    try:
        result = int(input("Quelle diagramme veux tu: 1- Un mois 2- Tous les mois  3- Par Année 4- Exit : " ))
    except ValueError:
        print("Error! This is not a number. Try again.")
    if (result == 1):
        month = input('Quelle est le mois souhaitez ?')
        createCurvesByMonth(month)
    if (result == 2):
        createCurvesAllMonth()
    if (result == 3):
        createCurvesByYear()

menu()


