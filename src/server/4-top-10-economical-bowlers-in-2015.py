import csv
from json import *

with open('../data/matches.csv', 'r') as matchCsvFile:

    matchDataList = list(csv.DictReader(matchCsvFile))

    def matches2015(match):

        return match['season'] == '2015'
    
    matchesPlayed2015 = list(filter(matches2015, matchDataList))

    def matchesIdsFun2015(match):

        return match['id']

    matchesIds2015 = list(map(matchesIdsFun2015, matchesPlayed2015))

with open('../data/deliveries.csv', 'r') as deliveryCsvFile:

    deliveryDataList = list(csv.DictReader(deliveryCsvFile))

    bowlersRunList = {}

    bowlersBowlList = {}

    bowlerEconomyList = {}

    for match in deliveryDataList:

        if match['match_id'] in matchesIds2015:

            if match['bowler'] in bowlersRunList:

                bowlersRunList[match['bowler']] += int(match['total_runs'])

                bowlersBowlList[match['bowler']] += 1

                bowlerEconomyList[match['bowler']] = round((bowlersRunList[match['bowler']]/bowlersBowlList[match['bowler']])*6, 2)

            else:

                bowlersRunList[match['bowler']] = int(match['total_runs'])

                bowlersBowlList[match['bowler']] = 1

                bowlerEconomyList[match['bowler']] = round((bowlersRunList[match['bowler']]/bowlersBowlList[match['bowler']])*6, 2)

    sortedEconomyList = dict(sorted(bowlerEconomyList.items(), key = lambda x: x[1]))

    topTenEconomyBowlers = dict(list(sortedEconomyList.items())[1:11])

with open('../public/output/4-top-10-economical-bowler-in-2015.json', 'w') as topTenEconomyBowlersJson:

    topTenEconomyBowlersJson.write(dumps(topTenEconomyBowlers))