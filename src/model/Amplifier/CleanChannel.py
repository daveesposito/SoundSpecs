'''
Created on Mar 13, 2015

@author: desposito
'''
from model.Utilities.Controls import Knob, Switch

class CleanChannel():
    '''
    Defines controls in the clean channel of the Marshall G80RCD amp.
    '''
    
    def __init__(self, gain=0.0, bass=0.0, mid=0.0, treble=0.0):
        '''
        Constructor
        '''
        try:
            gain_val = float(gain)
        except:
            raise TypeError("Invalid gain value: " + str(gain))
        
        try:
            bass_val = float(bass)
        except:
            raise TypeError("Invalid bass value: " + str(bass))
        
        try:
            mid_val = float(mid)
        except:
            raise TypeError("Invalid mid value: " + str(mid))
        
        try:
            treble_val = float(treble)
        except:
            raise TypeError("Invalid treble value: " + str(treble))
                    
        self.CleanType = Switch("Clean Type", "Crunch", "Clean", False)
        self.Gain = Knob("Gain", current_position=gain_val)
        self.Bass = Knob("Bass", current_position=bass_val)
        self.Mid = Knob("Mid", current_position=mid_val)
        self.Treble = Knob("Treble", current_position=treble_val)
        
    def Select_Crunch(self):
        '''
        Sets the channel to use the crunch circuit.
        '''
        self.CleanType.Turn_On()
        
    def Select_Clean(self):
        '''
        Sets the channel to use the clean circuit.
        '''
        self.CleanType.Turn_Off()
        
    def Current_Type(self):
        '''
        Determines which circuit the clean channel is using.
        '''
        return self.CleanType.Current_State_Name()