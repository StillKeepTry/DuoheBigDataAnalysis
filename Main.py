#coding=utf-8
'''
Created on 2015-5-4

@author: skt
'''

import numpy as np 
from DataDeal import ReadUserInfo, ReadUserloginDay, ReadUserGameOrder
import sys
import time
import function
import os
import Statistics

target = ['Datain']

userinfo, userlogindays, userGameOrder, games, user = None, None, None, set(), set()

user_game, game_user = dict(), dict()

# 数据读入部分

def DataConstruct():
    start = time.time()

    userinfos = ReadUserInfo.Readuserinfo()
    function.myfunction.filewrite(userinfos, 'Generate/userinfo.csv')
    print "User info : %d " % (len(userinfos))

    userlogindays = ReadUserloginDay.readUserloginDay()
    function.myfunction.filewrite(userlogindays, 'Generate/userlogindays.csv')
    print "User login day recoders : %d" % (len(userlogindays))
    
    userGameOrder = ReadUserGameOrder.readUserGameOrder()
    function.myfunction.filewrite(userGameOrder, 'Generate/userGameOrder.csv')
    print "User Game Orders : %d" % (len(userGameOrder))

    end = time.time()

    print "data preprocess step : " + str(end - start) + " seconds"

'''
挖掘用户与游戏之间的有用消息
logincount + oneday : clientID -- Game, 登录次数
successSmsCount : clientId -- Game, 支付情况
totalMoney : 总金额
smsCount : 总数量

构建用户与游戏之间的偏好度,通过已有值,可以采用的信息是用户点击,和用户支付金额,以及用户订单数量

定义 用户点击       :  alpha
定义 用户支付金额   :  beta
定义 用户订单数量   :  theta

保存游戏列表,其中在该阶段,游戏列表数量为27, 用户数为1197066
'''
def DataRead():    
    print "start to read data"
    start = time.time()
    
    for line in open("Generate/userinfo.csv"):
        clientId, Gamelist, createTime, updateTime = line.strip().split(",")
        Gamelist = Gamelist.split('|')
        user.add(clientId)
        for i in Gamelist:
            if i is not "":
                games.add(i)


    for line in open("Generate/userlogindays.csv"):
        appkey, clientId, oneday, logincount = line.strip().split(",")
        user.add(clientId)
        if appkey is not "":
            games.add(appkey)
            if clientId not in user_game:
                user_game[clientId] = dict()
            if appkey not in user_game[clientId]:
                user_game[clientId][appkey] = {'logincount': 0, 'smsCount': 0, 'totalMoney': 0}
            user_game[clientId][appkey]['logincount'] += int(logincount)

    
    for line in open("Generate/userGameOrder.csv"):
        clientId, appkey, status, successSmsCount, totalMoney, smsCount, successSmsCount, clientstatus = line.strip().split(",")
        user.add(clientId)
        if appkey is not "":
            games.add(appkey)
            if clientId not in user_game:
                user_game[clientId] = dict()
            if appkey not in user_game[clientId]:
                user_game[clientId][appkey] = {'logincount': 0, 'smsCount': 0, 'totalMoney': 0}
            user_game[clientId][appkey]['smsCount'] += int(smsCount)
            user_game[clientId][appkey]['totalMoney'] += int(totalMoney)
    
    end = time.time()
    print "data read cost " + str(end - start) + " seconds"

    if os.path.isfile("Generate/games.dat") == False:
        f = open("Generate/games.dat", "wb")
        for i in games:
            f.write(i)
            f.write("\n")
        f.close()
    
    if os.path.isfile("Generate/user.dat") == False:
        f = open("Generate/user.dat", "wb")
        for i in user:
            f.write(i)
            f.write("\n")
        f.close()

    print "用户集数目: %d\n游戏集数目: %d" % (len(user), len(games))

    f = open("Generate/user_game.dat", "wb")
    for (User, Games) in user_game.items():
        for (game, c) in Games.items():
            a = ','.join([User, game, str(c['logincount']), str(c['smsCount']), str(c['totalMoney'])])
            f.write(a)
            f.write("\n")
    f.close()

def DataUser():
    f = open("Generate/user_game.dat", "r")
    for line in f:
        user, appkey, logincount, smsCount, totalMoney = line.strip().split(",")
        if user not in user_game:
            user_game[user] = dict()
        if appkey not in user_game[user]:
            user_game[user][appkey] = {'logincount' : 0, 'smsCount': 0, 'totalMoney': 0}
        user_game[user][appkey]['logincount'] += int(logincount)
        user_game[user][appkey]['smsCount'] += int(smsCount)
        user_game[user][appkey]['totalMoney'] += int(totalMoney)
    Statistics.UserInfoStatistics.UsertoGameNum(user_game)

def Userfilter():
    f = open("Generate/user_file.dat", "w")

def Gamefilter():
    f = open("Generate/game_filter.dat", "w")


def DataGame():
    f = open("Generate/user_game.dat", "r")
    for line in f:
        user, appkey, logincount, smsCount, totalMoney = line.strip().split(",")
        if appkey not in game_user:
            game_user[appkey] = dict()
        if user not in game_user[appkey]:
            game_user[appkey][user] = {'logincount': 0, 'smsCount': 0, 'totalMoney': 0}
        game_user[appkey][user]['logincount'] += int(logincount)
        game_user[appkey][user]['smsCount'] += int(smsCount)
        game_user[appkey][user]['totalMoney'] += int(totalMoney)
    Statistics.UserInfoStatistics.GametoUserNum(game_user)
    
if __name__ == '__main__':
    args = sys.argv

    if "PreProcess" in args:
        DataConstruct()

    if "Datain" in args:
        DataRead()

    if "DataUser" in args:
        DataUser()

    if "DataGame" in args:
        DataGame()
