'''
Created on Mar 17, 2015

@author: desposito
'''
from Utilities.Controls import Knob

class IbanazBTBBass(object):
    '''
    classdocs
    '''

    def __init__(self, volume=10.0, pickup=0.0, bass=0.0, mid=0.0, treble=0.0):
        '''
        Constructor
        '''
        self.Volume = Knob("Volume", current_position=volume)
        self.Pickup = Knob("Pickup", -10, 10, pickup)
        self.Bass = Knob("Bass", -10, 10, bass)
        self.Mid = Knob("Mid", -10, 10, mid)
        self.Treble = Knob("Treble", -10, 10, treble)