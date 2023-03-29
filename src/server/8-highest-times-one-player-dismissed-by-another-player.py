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