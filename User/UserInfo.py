'''
Created on 2015-5-4

@author: skt
'''

class UserInfo(object):
    '''
    classdocs
    '''

    '''
    cliendId  : id to identity user 
    gamelist  : user has install the game lists
    status    : is regular or blacklist
    updateTime: user last update game time
    createTime: user first install game time
    '''

    def __init__(self, clientId, gamelist, status, updateTime, createTime):
        '''
        Constructor
        '''
        self.clientId = clientId
        self.gamelist = gamelist
        self.status = status
        self.updateTime = updateTime
        self.createTime = createTime
        


    def isActive(self):
        if self.updateTime == self.createTime:
            return True
        else:
            return False