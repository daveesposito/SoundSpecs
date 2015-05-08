'''
Created on Mar 17, 2015

@author: desposito
'''

from model.utilities.controls import Knob


class IbanezBTBBass():
    '''Models controls on the Ibanez BTB Bass.
    '''
    

    def __init__(self, volume=10.0, pickup=0.0, bass=0.0, mid=0.0, treble=0.0):
        '''Constructor
        '''
        
        self.volume = Knob("Volume", current_position=volume)
        self.pickup = Knob("Pickup", -10, 10, pickup)
        self.bass = Knob("Bass", -10, 10, bass)
        self.mid = Knob("Mid", -10, 10, mid)
        self.treble = Knob("Treble", -10, 10, treble)