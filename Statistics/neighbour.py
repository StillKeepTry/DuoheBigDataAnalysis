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
        b.append(a[i][1])
    return b
