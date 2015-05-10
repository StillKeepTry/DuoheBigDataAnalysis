#coding=utf-8
'''
Created on 2015-5-6

@author: skt
'''

import numpy as np 

'''
用户-游戏的影响因子
由以下参数组成
点击数, 支付金额, 购买订单

在 影响因子 方面, 
点击数最小,
订单数

alpha 对应 logincount
alpha = 0.1 
'''

def getFactor(logincount, smsCount, totalMoney):
    factor, alpha, beta, theta = 0.0, 0.0, 0.0, 0.0
    
    alpha = 0.1


def UsertoGameNum(user_game):
    num = [0] * 30
    for (User, Game) in user_game.items():
        num[len(Game)] += 1
    for i, v in enumerate(num):
        if v != 0:
            print "用户有 %d 条游戏记录行为的个数 : %d" % (i, v)

def GametoUserNum(game_user):
    for (Game, User) in game_user.items():
        print "appkey : {0:40} \t有 {1} 个" .format(Game, len(User))

def UsertoGameFilter(user_game, upperbound):
    f = open("Generate/user_filter.dat", "w")
    cnt = 0
    for (User, Games) in user_game.items():
        if len(Games) >= upperbound:
            for (game, c) in Games.items():
                a = ",".join([User, game, str(c['logincount']), str(c['smsCount']), str(c['totalMoney'])])
                f.write(a)
                f.write("\n")
        else:
            cnt = cnt + len(Games)
    f.close()
    print "过滤掉 %d 条用户" % (cnt)
