'''
Created on Mar 16, 2015

@author: desposito
'''
from model.Utilities.Controls import Knob, Switch
from model.Utilities.Connection import Connection

class Compressor():
    '''
    Models controls for Boss compressor pedal.
    '''

    def __init__(self, level=0.0, tone=0.0, attack=0.0, sustain=0.0):
        '''
        Constructor
        '''
        try:
            level_val = float(level)
        except:
            raise TypeError("Invalid level value: " + str(level))
        
        try:
            tone_val = float(tone)
        except:
            raise TypeError("Invalid tone value: " + str(tone))
        
        try:
            attack_val = float(attack)
        except:
            raise TypeError("Invalid attack value: " + str(attack))
        
        try:
            sustain_val = float(sustain)
        except:
            raise TypeError("Invalid sustain value: " + str(sustain))
        
        self.Active = Switch("Active", "On", "Off", False)
        self.Level = Knob("Level", current_position=level_val)
        self.Tone = Knob("Tone", current_position=tone_val)
        self.Attack = Knob("Attack", current_position=attack_val)
        self.Sustain = Knob("Threshold", current_position=sustain_val)
        self.ConnectedDevice = Connection()
        
    def Turn_On(self):
        '''
        Turns compressor on.
        '''
        self.Active.Turn_On()
        
    def Turn_Off(self):
        '''
        Turns compressor off.
        '''
        self.Active.Turn_Off()
    
    def Is_Active(self):
        '''
        True if compressor is on.  False if compressor is off.
        '''
        return self.Active.Current_State()
    
    def Get_Current_Active_State(self):
        '''
        "On" if compressor is on.  "Off" if compressor is off.
        '''
        return self.Active.Current_State_Name()