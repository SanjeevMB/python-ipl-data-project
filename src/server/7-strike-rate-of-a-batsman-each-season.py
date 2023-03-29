import csv
from json import *

with open('../data/matches.csv', 'r') as matchCsvFile:
    
    matchDataList = list(csv.DictReader(matchCsvFile))

    seasonId = {}

    for match in matchDataList:

        if match['season'] in seasonId:

            pass

        else:

            seasonId[match['id']] = match['season']

with open('../data/deliveries.csv', 'r') as deliveriesCsvFile:

    deliveryDataList = list(csv.DictReader(deliveriesCsvFile))

batsmanRuns = {}

batsmanBowls = {}

strikeRateOfBatsman = {}

for batsman in deliveryDataList:

    if batsman['batsman'] in strikeRateOfBatsman:

        if seasonId[batsman['match_id']] in strikeRateOfBatsman[batsman['batsman']]:

            batsmanRuns[batsman['batsman']][seasonId[batsman['match_id']]] += int(batsman["batsman_runs"])

            batsmanBowls[batsman['batsman']][seasonId[batsman['match_id']]] += 1

            strikeRateOfBatsman[batsman['batsman']][seasonId[batsman['match_id']]] = round((batsmanRuns[batsman['batsman']][seasonId[batsman['match_id']]]/batsmanBowls[batsman['batsman']][seasonId[batsman['match_id']]])*100, 2)

        else:

            strikeRateOfBatsman[batsman['batsman']][seasonId[batsman['match_id']]] = {} 

            batsmanBowls[batsman['batsman']] = {seasonId[batsman['match_id']]: 1}

            batsmanRuns[batsman['batsman']] = {seasonId[batsman['match_id']]: int(batsman['batsman_runs'])}

            strikeRateOfBatsman[batsman['batsman']][seasonId[batsman['match_id']]] = round((batsmanRuns[batsman['batsman']][seasonId[batsman['match_id']]]/batsmanBowls[batsman['batsman']][seasonId[batsman['match_id']]])*100, 2)

    else:
        
        strikeRateOfBatsman[batsman['batsman']] = {} 

        batsmanRuns[batsman['batsman']] = {seasonId[batsman['match_id']]: int(batsman['batsman_runs'])}

        batsmanBowls[batsman['batsman']] = {seasonId[batsman['match_id']]: 1}

        strikeRateOfBatsman[batsman['batsman']][seasonId[batsman['match_id']]] = round((batsmanRuns[batsman['batsman']][seasonId[batsman['match_id']]]/batsmanBowls[batsman['batsman']][seasonId[batsman['match_id']]])*100, 2)

with open('../public/output/7-strike-rate-of-a-batsman-each-season.json', 'w') as strikeRateEachBatsmanEachSeasonJson:

    strikeRateEachBatsmanEachSeasonJson.write(dumps(strikeRateOfBatsman))