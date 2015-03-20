'''
Created on Mar 19, 2015

@author: desposito
'''
from Utilities.Controls import Knob

class IMP2(object):
    '''
    Models controls on the IMP2 DI box.
    '''

    def __init__(self, level=10.0, connected_device=None):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)
        self.ConnectedDevice = connected_device