import csv
from json import *

with open('../data/matches.csv', 'r') as matchCsvFile:

    matchDataList = list(csv.DictReader(matchCsvFile))

    playerOfMatchAllMixed = {}

    for match in matchDataList:

        if match['season'] in playerOfMatchAllMixed:

            if match['player_of_match'] in playerOfMatchAllMixed[match['season']]:

                playerOfMatchAllMixed[match['season']][match['player_of_match']] += 1

            else:
                
                playerOfMatchAllMixed[match['season']][match['player_of_match']] = 1

        else:

            playerOfMatchAllMixed[match['season']] = {match['player_of_match']: 1}

    highestPlayerOfMatchEachSeason = {}

    bestEconomy = 0

    bestEconomyPlayer = ''

    for season in playerOfMatchAllMixed:

        for player in playerOfMatchAllMixed[season]:

            if playerOfMatchAllMixed[season][player] > bestEconomy:

                bestEconomy = playerOfMatchAllMixed[season][player]

                bestEconomyPlayer = player

                highestPlayerOfMatchEachSeason[season] = {bestEconomyPlayer: bestEconomy}   

        bestEconomy = 0                 

with open('../public/output/6-player-won-highest-number-player-of-match-each-season.json', 'w') as highestPlayerOfMatchJson:

    highestPlayerOfMatchJson.write(dumps(highestPlayerOfMatchEachSeason))