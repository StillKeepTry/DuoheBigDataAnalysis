'''
Created on 2015-5-4

@author: skt
'''

class UserGameOrder(object):
    '''
    classdocs
    '''    
    
    def __init__(self, clientId, status):
        '''
        Constructor
        '''
        self.clientId = clientId
        self.status = status
        
