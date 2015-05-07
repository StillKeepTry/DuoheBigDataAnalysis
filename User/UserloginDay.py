'''
Created on 2015-5-4

@author: skt
'''

class UserloginDay(object):
    '''
    classdocs
    '''

    '''
    clientId     : id to identity user
    activeUsernum: activeUsernum
    appkey
    loginCount   :
    day          :
    '''

    def __init__(self, clientId, appkey, day, loginCount):
        '''
        Constructor
        '''
        self.clientId = clientId
        self.appkey = appkey
        self.loginCount = loginCount
        self.day = day
        