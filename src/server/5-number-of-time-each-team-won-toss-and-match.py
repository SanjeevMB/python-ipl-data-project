import csv
from json import *

with open('../data/matches.csv', 'r') as matchCsvFile:

    matchDataList = list(csv.DictReader(matchCsvFile))

    eachTeamWonTossAndMatches = {}

    for match in matchDataList:

        if match['toss_winner'] == match['winner']:

            if match['winner'] in eachTeamWonTossAndMatches:

                eachTeamWonTossAndMatches[match['winner']] += 1

            else:

                eachTeamWonTossAndMatches[match['winner']] = 1

with open('../public/output/5-number-of-time-each-team-won-toss-and-won-match.json', 'w') as matchAndTossWonCountjson:

    matchAndTossWonCountjson.write(dumps(eachTeamWonTossAndMatches))