#!/usr/bin/env python
# coding=utf-8

'''
auther : skt
'''

import UserInfoStatistics
import dataset

def calcNearestNeighbour(userid, user, TopN, similar):
    a = []
    b = []
    for i, v in enumerate(user):    
        if i != userid:
            similarity = similar(user[userid], v)
            a.append([similarity, i])

    a.sort(key=lambda l:(l[0], l[1]), reverse=True)

    for i in range(0, TopN):
        b.append(a[i])
    return b

'''
User, 整体集
nearestneighbour, 近似邻
pos, 当前User
'''

def recommendation(User, nearestneighbour, pos, reverseGameIndex, Username, choose, upper=None):
    pred = []
    for i in range(len(User[pos])):
        pred.append([i, 0])
    for neighbour in nearestneighbour:
        similar, i = neighbour[0], neighbour[1]
        for j, v in enumerate(User[i]):
            pred[j][1] += v * similar
    for i, v in enumerate(User[pos]):
        if v > 0.0:
            pred[i][1] = 0
    pred.sort(key=lambda l:(l[1], l[0]), reverse=True)    
    ans = []
    for predict in pred:
        if predict[1] > choose and (upper == None or predict[1] < upper):
            ans.append([Username, reverseGameIndex[predict[0]]])
    return ans

def combine(User, UserIndex, reverseGameIndex, reverseUserIndex):
    pred = []

    for i in range(0, len(UserIndex)):
        nearestneighbour = calcNearestNeighbour(i, User, 5, UserInfoStatistics.Euclidean)
        pred = pred + recommendation(User, nearestneighbour, i, reverseGameIndex, reverseUserIndex[i], 0.08, upper=0.13)

    for i in range(0, len(UserIndex)):
        nearestneighbour = calcNearestNeighbour(i, User, 5, UserInfoStatistics.Pearson)
        pred = pred + recommendation(User, nearestneighbour, i, reverseGameIndex, reverseUserIndex[i], 0.12)
    
    a = set()
    for i in pred:
        if (i[0], i[1]) not in a:
            a.add((i[0], i[1]))
    pred = []

    for i in a:
        pred.append([i[0], i[1]])
    
    dataset.saveAns(pred)
    ans = dataset.getAns()
    
    print "基于用户, 融合最近邻和皮尔逊, F1值: %lf" % (ans)

def calc(User, UserIndex, reverseGameIndex, reverseUserIndex, TopN, similar, choose):
    pred = []
    for i in range(0, len(UserIndex)):
        nearestneighbour = calcNearestNeighbour(i, User, TopN, similar)
        pred = pred + recommendation(User, nearestneighbour, i, reverseGameIndex, reverseUserIndex[i], choose)
    dataset.saveAns(pred)
    ans = dataset.getAns()
    return ans


