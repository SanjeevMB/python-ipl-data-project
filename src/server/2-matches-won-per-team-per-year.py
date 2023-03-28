import csv
from json import *

with open('../data/matches.csv', 'r') as csvFile:

    matchData = list(csv.DictReader(csvFile))

    matchesWonPerTeamPerYear = {}

    for match in matchData:

        if match['winner'] in matchesWonPerTeamPerYear:

            if match['season'] in matchesWonPerTeamPerYear[match['winner']]:

                matchesWonPerTeamPerYear[match['winner']][match['season']] += 1

            else:

                matchesWonPerTeamPerYear[match['winner']][match['season']] = 1

        else:

            matchesWonPerTeamPerYear[match['winner']] = {}

            if match['season'] in matchesWonPerTeamPerYear[match['winner']]:

                matchesWonPerTeamPerYear[match['winner']][match['season']] += 1

            else:

                matchesWonPerTeamPerYear[match['winner']][match['season']] = 1

    strData = dumps(matchesWonPerTeamPerYear)

with open('../public/output/2-matches-won-per-team-per-year.json', 'w') as jsonData:

    jsonData.write(strData)