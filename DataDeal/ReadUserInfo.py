#coding=utf-8

'''
Created on 2015-5-4

@author: skt
'''

'''
过滤黑名单数据
'''
def Readuserinfo():
    f = open('Data/u_user_info.csv', 'r')
    features = []
    for line in f.readlines():
        feature = (line.strip().replace('"', '')).split(',')
        if feature[12] == '0':
            userinfo = [feature[0], feature[9], feature[10], feature[11]]
            features.append(userinfo)    
    f.close()
    return features
    
