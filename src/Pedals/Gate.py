'''
Created on Mar 16, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Switch

class Gate(object):
    '''
    classdocs
    '''


    def __init__(self, threshold=0.0, decay=0.0):
        '''
        Constructor
        '''
        try:
            threshold_val = float(threshold)
        except:
            raise TypeError("Invalid threshold value: " + str(threshold))
        
        try:
            decay_val = float(decay)
        except:
            raise TypeError("Invalid decay value: " + str(decay))
        
        self.Active = Switch("Active", "On", "Off", False)
        self.Mode = Switch("Mode", "Mute", "Gate", False)
        self.Threshold = Knob("Threshold", current_position=threshold_val)
        self.Decay = Knob("Decay", current_position=decay_val)
        
    def Turn_On(self):
        self.Active.Turn_On()
        
    def Turn_Off(self):
        self.Active.Turn_Off()
    
    def Is_Active(self):
        return self.Active.Current_State()
    
    def Get_Current_Active_State(self):
        return self.Active.Current_State_Name()
    
    def Set_Mode_To_Mute(self):
        self.Mode.Turn_On()
        
    def Set_Mode_To_Gate(self):
        self.Mode.Turn_Off()
        
    def Get_Current_Mode(self):
        return self.Mode.Current_State_Name()