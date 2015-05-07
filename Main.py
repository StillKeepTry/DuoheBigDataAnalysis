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

target = ['Datain']

userinfo, userlogindays, userGameOrder, games, user = None, None, None, set(), set()

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
status: clientID -- Game, 是否 黑名单
logincount + oneday : clientID -- Game, 登录次数
successSmsCount : clientId -- Game, 支付情况

保存游戏列表,其中在该阶段,游戏列表数量为27, 用户数为1197066
'''
def DataRead():    
    start = time.time()
    
    for line in open("Generate/userinfo.csv"):
        clientId, Gamelist, status, createTime, updateTime = line.strip().split(",")
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
    
    for line in open("Generate/userGameOrder.csv"):
        clientId, appkey, status, successSmsCount, totalMoney, smsCount, successSmsCount, clientstatus = line.strip().split(",")
        user.add(clientId)
        if appkey is not "":
            games.add(appkey)
    
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

    print len(user)

if __name__ == '__main__':
    args = sys.argv

    if "PreProcess" in args:
        DataConstruct()
    
    if "Datain" in args:
        DataRead()
