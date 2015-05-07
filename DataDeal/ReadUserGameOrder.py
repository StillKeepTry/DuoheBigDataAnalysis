'''
Created on 2015-5-4

@author: skt
'''

import csv

'''
clientId
appKey
status
successMoney
totalMoney
smsCount
successSmsCount
clientstatus

'''

def readUserGameOrder():
    features = []
    f = file('Data/u_games_order.csv', 'rb')
    reader = csv.reader(f)
    for line in reader:
        feature = line
        if len(feature) == 26:
            if feature[1] != "Unknown":
                userGameOrder = [feature[1], feature[3], feature[5], feature[10], feature[11], feature[12], feature[13], feature[15]]
            features.append(userGameOrder)
    return features
        