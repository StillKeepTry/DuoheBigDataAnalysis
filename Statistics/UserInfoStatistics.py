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
'''

def getFactor(logincount, smsCount, totalMoney):
    factor, alpha, beta, theta = 0.0


def UsertoGameNum(user_game):
    num = [0] * 30
    for (User, Game) in user_game.items():
        num[len(Game)] += 1
    for i, v in enumerate(num):
        if v != 0:
            print "用户有 %d 条游戏记录行为的个数 : %d" % (i, v)

def GametoUserNum(game_user):
    for (Game, User) in game_user.items():
        print "appkey : %s \t有%d" % (Game, len(User))
