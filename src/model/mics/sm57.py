'''
Created on Mar 18, 2015

@author: desposito
'''

from model.mics.mic import Mic


class SM57(Mic):
    '''Wrapper class for SM57 model.  Operates as a generic mic with no 
       additional special behavior.
    '''


    def __init__(self, name):
        '''Constructor
        '''
        
        Mic.__init__(self, name)