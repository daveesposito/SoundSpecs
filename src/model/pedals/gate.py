'''
Created on Mar 16, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Switch
from model.utilities.connection import Connection


class Gate():
    '''Models controls on Boss Noise Gate pedal.
    '''


    def __init__(self, threshold=0.0, decay=0.0):
        '''Constructor
        '''
        
        try:
            threshold_val = float(threshold)
        except:
            raise TypeError("Invalid threshold value: {0}"\
                            .format(str(threshold)))
        
        try:
            decay_val = float(decay)
        except:
            raise TypeError("Invalid decay value: {0}".format(str(decay)))
        
        self.active = Switch("Active", "On", "Off", False)
        self.mode = Switch("Mode", "Mute", "Gate", False)
        self.threshold = Knob("Threshold", current_position=threshold_val)
        self.decay = Knob("Decay", current_position=decay_val)
        self.connected_device = Connection("Input")
        self.send = Send("Send")
        self.return_ = Connection("Return")
        
    def turn_on(self):
        '''Activates pedal function.
        '''
        
        self.active.turn_on()
        
    def turn_off(self):
        '''Deactivates pedal function.
        '''
        
        self.active.turn_off()
    
    def is_active(self):
        '''True if gate is active.  False if gate is inactive.
        '''
        
        return self.active.state
    
    def get_current_active_state(self):
        '''"On" if gate is active.  "Off" if gate is inactive.
        '''
        
        return self.active.state_name()
    
    def set_mode_to_mute(self):
        '''Sets mode switch to Mute.
        '''
        
        self.mode.turn_on()
        
    def set_mode_to_gate(self):
        '''Sets mode switch to Reduction.
        '''
        
        self.mode.turn_off()
        
    def get_current_mode(self):
        '''"Mute" if in mute mode. "Gate" if in gate mode.
        '''
        
        return self.mode.state_name()
    
    
class Send():
    '''Send object for the effects loop of the noise gate.  This is what will 
       attach to other input devices.
    '''
    
    
    def __init__(self, name):
        self.name = name
