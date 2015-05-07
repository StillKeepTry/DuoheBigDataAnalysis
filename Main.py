#coding=utf-8

import numpy as np 
from DataDeal import ReadUserInfo, ReadUserloginDay, ReadUserGameOrder
import csv
import sys
import time

target = ['Datain']

userinfo, userlogindays, userGameOrder, games = None, None, None, set()

# 数据读入部分

def DataConstruct():
    start = time.time()

    userinfos = ReadUserInfo.Readuserinfo()
    csvfile = file('Generate/userinfo.csv', 'wb')
    f = csv.writer(csvfile)
    for i in userinfos:
        f.writerow(i)
    csvfile.close()
    print "User amounts : %d" % (len(userinfos))

    userlogindays = ReadUserloginDay.readUserloginDay()
    csvfile = file('Generate/userlogindays.csv', 'wb')
    f = csv.writer(csvfile)
    for i in userlogindays:
        f.writerow(i)
    csvfile.close()
    print "User login day recoders : %d" % (len(userlogindays))
    
    userGameOrder = ReadUserGameOrder.readUserGameOrder()
    csvfile = file('Generate/userGameOrder.csv', 'wb')
    f = csv.writer(csvfile)
    for i in userGameOrder:
    
        f.writerow(i)

    csvfile.close()

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
