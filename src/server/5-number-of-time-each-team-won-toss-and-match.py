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



iplMatch = {
    "id": "1", 
    "season": "2017", 
    "city": "Hyderabad", 
    "date": "2017-04-05", 
    "team1": "Sunrisers Hyderabad", 
    "team2": "Royal Challengers Bangalore", 
    "toss_winner": "Royal Challengers Bangalore", 
    "toss_decision": "field", 
    "result": "normal", 
    "dl_applied": "0", 
    "winner": "Sunrisers Hyderabad", 
    "win_by_runs": "35", 
    "win_by_wickets": "0", 
    "player_of_match": "Yuvraj Singh", 
    "venue": "Rajiv Gandhi International Stadium, Uppal", 
    "umpire1": "AY Dandekar", 
    "umpire2": "NJ Llong", 
    "umpire3": ""
    }