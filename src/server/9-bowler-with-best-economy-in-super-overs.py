import csv
from json import *

with open('../data/deliveries.csv', 'r') as deliveryCsvFile:

    deliveryDataList = list(csv.DictReader(deliveryCsvFile))

    bowlerBowlCount = {}

    bowlerRunCount = {}

    bowlerEconomySuperOver = {}

    for match in deliveryDataList:

        if match['is_super_over'] == '1':

            if match['bowler'] in bowlerBowlCount:

                bowlerBowlCount[match['bowler']] += int(match['total_runs'])

                bowlerRunCount[match['bowler']] += 1

                bowlerEconomySuperOver[match['bowler']] = round((bowlerBowlCount[match['bowler']]/bowlerRunCount[match['bowler']])*6, 2)

            else:

                bowlerBowlCount[match['bowler']] = int(match['total_runs'])

                bowlerRunCount[match['bowler']] = 1

                bowlerEconomySuperOver[match['bowler']] = round((bowlerBowlCount[match['bowler']]/bowlerRunCount[match['bowler']])*6, 2)

    sortedEconomySuperOver = dict(sorted(bowlerEconomySuperOver.items(), key = lambda x: x[1]))

    bestEconomyInSuperOver = dict(list(sortedEconomySuperOver.items())[0:1])

with open('../public/output/9-bowler-with-best-economy-in-super-overs.json', 'w') as bestEconomyInSuperOverJson:

    bestEconomyInSuperOverJson.write(dumps(bestEconomyInSuperOver))