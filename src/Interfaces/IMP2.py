'''
Created on Mar 19, 2015

@author: desposito
'''
from Utilities.Controls import Knob

class IMP2(object):
    '''
    classdocs
    '''

    def __init__(self, level=10.0, connected_device=None):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)
        self.ConnectedDevice = connected_device