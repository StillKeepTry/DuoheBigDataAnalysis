#coding=utf-8
'''
Created on 2015-5-4

@author: skt
'''


import numpy as np 
from DataDeal import ReadUserInfo, ReadUserloginDay, ReadUserGameOrder
import csv
import sys
import time
import function

target = ['Datain']

userinfo, userlogindays, userGameOrder, games = None, None, None, set()

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

def DataRead():    
    start = time.time()
    
    for line in open("Generate/userinfo.csv"):
        clientId, Gamelist, status, createTime, updateTime = line.strip().split(",")
        Gamelist = Gamelist.split('|')
        for i in Gamelist:
            if i is not "":
                games.add(i)

    end = time.time()
    print "data read cost " + str(end - start) + "seconds"

    for line in open("Generate/userlogindays.csv"):
        appkey, clientId, oneday, logincount = line.strip().split(",")
        if appkey is not "":
            games.add(appkey)
    
    cnt = 0

    for line in open("Generate/userGameOrder.csv"):

        cnt += 1
        clientId, appkey, status, successSmsCount, totalMoney, smsCount, successSmsCount, clientstatus = line.strip().split(",")
        if appkey is not "":
            games.add(appkey)
    
    '''
    保存游戏列表,其中该阶段,游戏列表数量为27
    '''
    f = open("Generate/games.dat", "wb")
    for i in games:
        f.write(i)
        f.write("\n")
    f.close()

if __name__ == '__main__':
    args = sys.argv

    if "PreProcess" in args:
        DataConstruct()
    
    if "Datain" in args:
        DataRead()
