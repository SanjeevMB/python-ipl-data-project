import csv
from json import *

try:

    with open('../data/deliveries.csv', 'r') as deliveryCsvFile:

        deliveryDataList = list(csv.DictReader(deliveryCsvFile))

    print('data stored successfully in deliveryDataList')

except FileNotFoundError:

    print('Error : write the correct file name')

except ValueError:

    print('Error : Incorrect value of file mode')

except NameError:

    print('Error: wirte the correct name')

except AttributeError:

    print('Error : write a correct method')

bowlerBowlCount = {}

bowlerRunCount = {}

bowlerEconomySuperOver = {}

try:

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
                
except TypeError:

    print('Error : data type is not appropriate')

except NameError:

    print('Error: wirte the correct name')

except KeyError:

    print('Error: write correct keyword')

sortedEconomySuperOver = dict(sorted(bowlerEconomySuperOver.items(), key = lambda x: x[1]))

bestEconomyInSuperOver = dict(list(sortedEconomySuperOver.items())[0:1])

try:

    with open('../public/output/9-bowler-with-best-economy-in-super-overs.json', 'w') as bestEconomyInSuperOverJson:
        
        bestEconomyInSuperOverJson.write(dumps(bestEconomyInSuperOver))

        print('Successfully data wirtten in the output file')

except FileNotFoundError:

    print('Error : File path is not correct')

except ValueError:

    print('Error : Incorrect value of file mode')

except TypeError:

    print('Error : Convert the data to the str type')

except AttributeError:

    print('Error : write a correct method')