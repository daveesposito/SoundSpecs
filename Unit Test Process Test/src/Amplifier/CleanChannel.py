'''
Created on Mar 13, 2015

@author: desposito
'''
from Amplifier.Controls import Knob, Switch

class CleanChannel(object):
    '''
    classdocs
    '''
    
    def __init__(self, gain=0.0, bass=0.0, treble=0.0):
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
            treble_val = float(treble)
        except:
            raise TypeError("Invalid treble value: " + str(treble))
                    
        self.CleanType = Switch("Clean Type", "Crunch", "Clean", False)
        self.Gain = Knob("Gain", current_position=gain_val)
        self.Bass = Knob("Bass", current_position=bass_val)
        self.Treble = Knob("Treble", current_position=treble_val)
        
    def Select_Crunch(self):
        self.CleanType.Turn_On()
        
    def Select_Clean(self):
        self.CleanType.Turn_Off()
        
    def Current_Type(self):
        return self.CleanType.Current_State_Name()