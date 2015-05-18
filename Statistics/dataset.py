#!/usr/bin/env python
# coding=utf-8

'''
auther : skt
'''

def DatasetByFilterOneUserRecord(user_game):
    fdata = open("test/test.dat", "w")
    fpredict = open("test/predict.dat", "w")
    
    for (User, Game) in user_game.items():
        n = len(Game)
        m = n / 4
        cnt = 0
        for (game, c) in Game.items():
            a = ",".join([User, game, str(c['logincount']), str(c['smsCount']), str(c['totalMoney'])])
            b = ",".join([User, game])
            cnt += 1
            if cnt <= m:
                fpredict.write(b)
                fpredict.write("\n")
            else:
                fdata.write(a)
                fdata.write("\n")
    fdata.close()
    fpredict.close()

def DatasetByFilterOnFile(filename):
    f = open(filename, 'r')
    user_game = dict()
    for line in f:
        user, appkey, logincount, smsCount, totalMoney = line.strip().split(",")
        if user not in user_game:
            user_game[user] = dict()
        if appkey not in user_game[user]:
            user_game[user][appkey] = {'logincount' : 0, 'smsCount' : 0, 'totalMoney' : 0}
        user_game[user][appkey]['logincount'] += int(logincount)
        user_game[user][appkey]['smsCount'] += int(smsCount)
        user_game[user][appkey]['totalMoney'] += int(totalMoney)
    DatasetByFilterOneUserRecord(user_game)

def saveAns(user_game):
    f = open("test/ans.dat", "w")
    for i in user_game:
        a = ",".join(i)
        f.write(a)
        f.write("\n")
    f.close()

def getAns():
    predict = open("test/predict.dat", "r")
    ans = open("test/ans.dat", "r")

    a, b = set(), set()

    for line in predict:
        user, game = line.strip().split(",")
        a.add((user, game))

    c = 0

    for line in ans:
        user, game = line.strip().split(",")
        b.add((user, game))
        if (user, game) in a:
            c += 1

    a1 = c * 1.0 / len(a)
    a2 = c * 1.0 / len(b)

    a3 = 2.0 * a2 * a1 / (a1 + a2)
    return a3
