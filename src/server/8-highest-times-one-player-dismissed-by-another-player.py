import csv
from json import *

with open('../data/deliveries.csv', 'r') as deliveryCsvFile:

    deliveryDataList = list(csv.DictReader(deliveryCsvFile))

    allDismissalForAllPlayers = {}

    for dismiss in deliveryDataList:

        if dismiss['player_dismissed'] == '':

            pass

        else:

            if dismiss['player_dismissed'] in allDismissalForAllPlayers:

                if (dismiss['dismissal_kind'] == 'run out' or dismiss['dismissal_kind'] == 'stumped') and dismiss['fielder'] in allDismissalForAllPlayers[dismiss['player_dismissed']]:

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['fielder']] += 1

                elif (dismiss['dismissal_kind'] == 'lbw' or dismiss['dismissal_kind'] == 'bowled' or dismiss['dismissal_kind'] == 'caught and bowled' or dismiss['dismissal_kind'] == 'caught') and dismiss['bowler'] in allDismissalForAllPlayers:

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['bowler']] = 1           

                elif dismiss['dismissal_kind'] == 'run out' or dismiss['dismissal_kind'] == 'stumped':

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['fielder']] = 1 
                
                elif dismiss['dismissal_kind'] == 'lbw' or dismiss['dismissal_kind'] == 'bowled' or dismiss['dismissal_kind'] == 'caught and bowled' or dismiss['dismissal_kind'] == 'caught':

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['bowler']] = 1           

            else:                

                allDismissalForAllPlayers[dismiss['player_dismissed']] = {}  
                
                if (dismiss['dismissal_kind'] == 'run out' or dismiss['dismissal_kind'] == 'stumped'):

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['fielder']] = 1
                
                else:

                    allDismissalForAllPlayers[dismiss['player_dismissed']][dismiss['bowler']] = 1 

dismissedPlayer = ''
filder = ''
highestTime =  0

highestDismissedPlayer = {}

for player in allDismissalForAllPlayers:

    for anotherPlayer in allDismissalForAllPlayers[player]:

        if allDismissalForAllPlayers[player][anotherPlayer] > highestTime:

            dismissedPlayer = player

            filder = anotherPlayer

            highestTime = allDismissalForAllPlayers[player][anotherPlayer]

highestDismissedPlayer[dismissedPlayer] = highestTime

with open('../public/output/8-highest-times-one-player-dismissed-by-another-player.json', 'w') as highestDismissedPlayerJson:

    highestDismissedPlayerJson.write(dumps(highestDismissedPlayer))

iplDelivery = {
    "match_id": "1", 
    "inning": "1", 
    "batting_team": "Sunrisers Hyderabad", 
    "bowling_team": "Royal Challengers Bangalore", 
    "over": "1", 
    "ball": "1", 
    "batsman": "DA Warner", 
    "non_striker": "S Dhawan", 
    "bowler": "TS Mills", 
    "is_super_over": "0", 
    "wide_runs": "0", 
    "bye_runs": "0", 
    "legbye_runs": "0", 
    "noball_runs": "0", 
    "penalty_runs": "0", 
    "batsman_runs": "0", 
    "extra_runs": "0", 
    "total_runs": "0", 
    "player_dismissed": "", 
    "dismissal_kind": "", 
    "fielder": ""
    }