'''
Created on Apr 9, 2015

@author: desposito
'''


class Connection():
    '''Provides an object for setting a connection in a device.
    '''


    def __init__(self, name="No Connection", device=None):
        '''Constructor
        '''
        
        self.name = name
        self.device = device