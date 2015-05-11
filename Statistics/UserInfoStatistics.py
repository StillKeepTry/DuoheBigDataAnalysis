#coding=utf-8
'''
Created on 2015-5-6

@author: skt
'''

import math

'''
用户-游戏的影响因子
由以下参数组成
点击数, 支付金额, 购买订单

我定义用户-游戏的偏好度为
购买概率 * 购买金额 + 点击数 * x

购买概率 由 点击数 和 购买订单数决定

在 影响因子 方面, 
点击数最小,
订单数则表示出用户可能会频繁购买
支付金额则表示用户支付的概况

alpha 对应 logincount
alpha = 0.1 

beta 对应 订单数
beta = 0.5

theta 对应支付金额
theta = 1.0
'''

def getFactor(logincount, smsCount, totalMoney):
    logincount = int(logincount)
    smsCount = int(smsCount)
    totalMoney = int(totalMoney)
    factor, alpha, beta, theta, x  = 0.0, 0.2, 0.5, 1.0, 5.0
    factor = (alpha * logincount + beta * smsCount) * (totalMoney + x ) * theta
    return factor / 10.0

def UsertoGameNum(user_game):
    num = [0] * 30
    for (User, Game) in user_game.items():
        num[len(Game)] += 1
    for i, v in enumerate(num):
        if v != 0:
            print "用户有 %d 条游戏记录行为的个数 : %d" % (i, v)

def GametoUserNum(game_user):
    for (Game, User) in game_user.items():
        print "appkey : {0:40} \t有 {1} 个".format(Game, len(User))
    print "\n共有%d条游戏" % (len(game_user))

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

# 欧几里得
def Euclidean(A, B):
    n = len(A)
    sum = 0.0
    for i in range(0, n):
        sum = sum + (A[i] - B[i]) * (A[i] - B[i])
    sum = math.sqrt(sum)
    return 1.0 / (1.0 + sum)

# 皮尔逊
def Pearson(A, B):
    n = len(A)
    xy, x, y, x2, y2 = 0.0, sum(A), sum(B), 0.0, 0.0
    for i in range(0, n):
        xy = xy + A[i] * B[i]
        x2 = x2 + A[i] * A[i]
        y2 = y2 + B[i] * B[i]
    sum = (1.0 * n * xy - x * y) / (math.sqrt(n * x2 - x * x) * math.sqrt(n * y2 - y * y))
    return sum

# 余弦
def Cosine(A, B):
    n = len(A)
    xy, x2, y2 = 0.0, 0.0, 0.0
    for i in range(0, n):
        xy = xy + A[i] * B[i]
        x2 = x2 + A[i] * A[i]
        y2 = y2 + B[i] * B[i]
    return (1.0 * xy) / (math.sqrt(x2) * math.sqrt(y2))

# Tanimono
def Tanimono(A, B):
    n = len(A)
    xy, x2, y2 = 0.0, 0.0, 0.0
    for i in range(0, n):
        xy = xy + A[i] * B[i]
        x2 = x2 + A[i] * A[i]
        y2 = y2 + B[i] * B[i]
    return (xy) / (math.sqrt(x2) + math.sqrt(y2) - xy)



