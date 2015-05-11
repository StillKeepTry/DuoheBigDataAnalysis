'''
Created on 2015-5-7

@author: skt
'''

import csv

def filewrite(samples, filename):
    csvfile = file(filename, 'wb')
    f = csv.writer(csvfile)
    for i in samples:
        f.writerow(i)
    csvfile.close()
    
def getUserIndex(filename):
    User, count = dict(), 0
    f = open(filename, "r")
    for line in f:
        user, appkey, logincount, smsCount, totalMoney = line.strip().split(",")
        if user not in User:
            User[user] = count
            count += 1
    return User

def getGameIndex(filename):
    Game, count = dict(), 0
    f = open(filename, "r")
    for line in f:
        user, appkey, logincount, smsCount, totalMoney = line.strip().split(",")
        if appkey not in Game:
            Game[appkey] = count
            count += 1
    return Game
