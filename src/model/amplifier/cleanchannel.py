'''
Created on Mar 13, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Switch


class CleanChannel():
    '''Defines controls in the clean channel of the Marshall G80RCD amp.
    '''
    
    
    def __init__(self, gain=0.0, bass=0.0, mid=0.0, treble=0.0):
        '''Constructor
        '''
    
        gain_val = self._is_value_float(gain)
        bass_val = self._is_value_float(bass)
        mid_val = self._is_value_float(mid)
        treble_val = self._is_value_float(treble)
                            
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
    
    def _is_value_float(self, value):
        '''Ensure that the provided value can be reprented as a float.
        '''
        
        try:
            return float(value)
        except:
            raise TypeError("Invalid input: {0}".format(value))
        