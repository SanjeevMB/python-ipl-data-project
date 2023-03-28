import csv 
from json import *

with open('../data/matches.csv', 'r') as csvFile:

    matchDataList = list(csv.DictReader(csvFile))

    matchesPerYear = {}

    for match in matchDataList:

        if match['season'] in matchesPerYear:

            matchesPerYear[match['season']] += 1

        else:

            matchesPerYear[match['season']] = 1

    strData = dumps(matchesPerYear)

with open('../public/output/1-matches-per-years.json', 'w') as jsonData:

    jsonData.write(strData)