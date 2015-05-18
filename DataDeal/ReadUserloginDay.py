'''
Created on 2015-5-4

@author: skt
'''

def readUserloginDay():
    features = []
    f = open('Data/u_user_login_day.csv', 'r')
    for line in f.readlines():
        feature = (line.strip().replace('"', '')).split(',')
        if feature[3] != "null" and int(feature[6]) <= 1000 and feature[3] != "Unknown" and feature[3] != "0":
            userloginday = [feature[2], feature[3], feature[4], feature[6]]
            features.append(userloginday)
    return features
