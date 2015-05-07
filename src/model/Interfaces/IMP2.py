'''
Created on Mar 19, 2015

@author: desposito
'''
from model.utilities.controls import Knob
from model.utilities import connection.Connection

class IMP2():
    '''
    Models controls on the IMP2 DI box.
    '''

    def __init__(self, level=10.0):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)
        self.ConnectedDevice = connection()