import csv
from json import *

with open('../data/matches.csv', 'r') as matchCsvFile:

    matchDataList = list(csv.DictReader(matchCsvFile))

    def mathces2016 (match):

        return match['season'] == '2016'        

    matches2016 = list(filter(mathces2016, matchDataList))

    def ids2016 (match):

        return match['id']

    mathcIds2016 = list(map(ids2016, matches2016))

with open('../data/deliveries.csv', 'r') as deliveryCsvFile:

    deliveryDataList = list(csv.DictReader(deliveryCsvFile))

    extraRunsPerTeamIn2016 = {}

    for match in deliveryDataList:

        if match['match_id'] in mathcIds2016:

            if match['bowling_team'] in extraRunsPerTeamIn2016:

                extraRunsPerTeamIn2016[match['bowling_team']] += int(match['extra_runs'])

            else:

                extraRunsPerTeamIn2016[match['bowling_team']] = int(match['extra_runs'])

    # print(extraRunsPerTeamIn2016)

    extraRunsStr = dumps(extraRunsPerTeamIn2016)

with open('../public/output/3-extra-runs-conceded-per-team-in-2016.json', 'w') as jsonDelvery:

    jsonDelvery.write(extraRunsStr)