#!/usr/bin/env python
# coding=utf-8

'''
auther : skt
'''

import UserInfoStatistics

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

def recommendation(User, nearestneighbour, pos, reverseGameIndex, Username):
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
        if predict[1] > 0.05:
            ans.append([Username, reverseGameIndex[predict[0]]])
    return ans
