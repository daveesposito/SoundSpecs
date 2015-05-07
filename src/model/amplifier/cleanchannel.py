'''
Created on Mar 13, 2015

@author: desposito
'''

from model.Utilities.Controls import Knob, Switch


class CleanChannel():
    '''Defines controls in the clean channel of the Marshall G80RCD amp.
    '''
    
    
    def __init__(self, gain=0.0, bass=0.0, mid=0.0, treble=0.0):
        '''Constructor
        '''
    
        try:
            gain_val = float(gain)
        except:
            raise TypeError("Invalid gain value: {0}".format(str(gain)))
        
        try:
            bass_val = float(bass)
        except:
            raise TypeError("Invalid bass value: {0}".format(str(bass)))
        
        try:
            mid_val = float(mid)
        except:
            raise TypeError("Invalid mid value: {0}".format(str(mid)))
        
        try:
            treble_val = float(treble)
        except:
            raise TypeError("Invalid treble value: {0}".format(str(treble)))
                    
        self.clean_type = Switch("Clean Type", "Crunch", "Clean", False)
        self.gain = Knob("Gain", current_position=gain_val)
        self.bass = Knob("Bass", current_position=bass_val)
        self.mid = Knob("Mid", current_position=mid_val)
        self.treble = Knob("Treble", current_position=treble_val)
        
    def select_crunch(self):
        '''Sets the channel to use the crunch circuit.
        '''
        
        self.clean_type.turn_on()
        
    def select_clean(self):
        '''Sets the channel to use the clean circuit.
        '''
        
        self.clean_type.turn_off()
        
    def current_type(self):
        '''Determines which circuit the clean channel is using.
        '''
        
        return self.clean_type.state_name()