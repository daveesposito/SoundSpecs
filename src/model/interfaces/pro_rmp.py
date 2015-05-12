'''
Created on Mar 27, 2015

@author: Dave
'''

from model.utilities.controls import Knob, Switch
from model.utilities.connection import Connection


class ProRMP():
    '''Models Input and control on the Radial ProRMP Reamp box.
    '''
    

    def __init__(self, level=10.0, lift=False):
        '''Constructor
        '''
        
        self.level = Knob("Level", current_position=level)
        self.lift = Switch("Lift", state=lift)
        self.connected_device = Connection()
        