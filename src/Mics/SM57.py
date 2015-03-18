'''
Created on Mar 18, 2015

@author: desposito
'''
from Mics.Mic import Mic

class SM57(Mic):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        Mic.__init__(self, name)