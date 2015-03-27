'''
Created on Mar 27, 2015

@author: Dave
'''
from model.Utilities.Controls import Knob, Switch

class ProRMP(object):
    '''
    Models Input and control on the Radial ProRMP Reamp box.
    '''

    def __init__(self, level=10.0, lift=False, connected_device=None):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)
        self.Lift = Switch("Lift", current_state=lift)
        self.ConnectedDevice = connected_device