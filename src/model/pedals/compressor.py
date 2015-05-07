'''
Created on Mar 16, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Switch
from model.utilities.connection import Connection


class Compressor():
    '''Models controls for Boss compressor pedal.
    '''


    def __init__(self, level=0.0, tone=0.0, attack=0.0, sustain=0.0):
        '''Constructor
        '''
        
        try:
            level_val = float(level)
        except:
            raise TypeError("Invalid level value: {0}".format(str(level)))
        
        try:
            tone_val = float(tone)
        except:
            raise TypeError("Invalid tone value: {0}".format(str(tone)))
        
        try:
            attack_val = float(attack)
        except:
            raise TypeError("Invalid attack value: {0}".format(str(attack)))
        
        try:
            sustain_val = float(sustain)
        except:
            raise TypeError("Invalid sustain value: {0}".format(str(sustain)))
        
        self.active = Switch("Active", "On", "Off", False)
        self.level = Knob("Level", current_position=level_val)
        self.tone = Knob("Tone", current_position=tone_val)
        self.attack = Knob("Attack", current_position=attack_val)
        self.sustain = Knob("Threshold", current_position=sustain_val)
        self.connected_device = Connection("Input")
        
    def turn_on(self):
        '''Turns compressor on.
        '''
        
        self.active.turn_on()
        
    def turn_off(self):
        '''Turns compressor off.
        '''
        
        self.active.turn_off()
    
    def is_active(self):
        '''True if compressor is on.  False if compressor is off.
        '''
        
        return self.active.state
    
    def get_current_active_state(self):
        '''"On" if compressor is on.  "Off" if compressor is off.
        '''
        
        return self.active.state_name()
    