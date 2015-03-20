'''
Created on Mar 16, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Switch

class Compressor(object):
    '''
    Models controls for Boss compressor pedal.
    @todo: fix parameters to match control names on pedal.
    '''

    def __init__(self, threshold=0.0, tone=0.0, attack=0.0, level=0.0, connected_device=None):
        '''
        Constructor
        '''
        try:
            threshold_val = float(threshold)
        except:
            raise TypeError("Invalid threshold value: " + str(threshold))
        
        try:
            tone_val = float(tone)
        except:
            raise TypeError("Invalid tone value: " + str(tone))
        
        try:
            attack_val = float(attack)
        except:
            raise TypeError("Invalid attack value: " + str(attack))
        
        try:
            level_val = float(level)
        except:
            raise TypeError("Invalid level value: " + str(level))
        
        self.Active = Switch("Active", "On", "Off", False)
        self.Threshold = Knob("Threshold", current_position=threshold_val)
        self.Tone = Knob("Tone", current_position=tone_val)
        self.Attack = Knob("Attack", current_position=attack_val)
        self.Level = Knob("Level", current_position=level_val)
        self.ConnectedDevice = connected_device
        
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