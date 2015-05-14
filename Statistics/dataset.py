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
