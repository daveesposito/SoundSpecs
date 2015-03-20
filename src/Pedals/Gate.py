'''
Created on Mar 16, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Switch

class Gate(object):
    '''
    Models controls on Boss Noise Gate pedal.
    '''

    def __init__(self, threshold=0.0, decay=0.0, connected_device=None, return_input=None):
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
        self.ConnectedDevice = connected_device
        self.Send = Send()
        self.Return = return_input
        
    def Turn_On(self):
        '''
        Activates pedal function.
        '''
        self.Active.Turn_On()
        
    def Turn_Off(self):
        '''
        Deactivates pedal function.
        '''
        self.Active.Turn_Off()
    
    def Is_Active(self):
        '''
        True if gate is active.  False if gate is inactive.
        '''
        return self.Active.Current_State()
    
    def Get_Current_Active_State(self):
        '''
        "On" if gate is active.  "Off" if gate is inactive.
        '''
        return self.Active.Current_State_Name()
    
    def Set_Mode_To_Mute(self):
        '''
        Sets mode switch to Mute.
        '''
        self.Mode.Turn_On()
        
    def Set_Mode_To_Gate(self):
        '''
        Sets mode switch to Reduction.
        '''
        self.Mode.Turn_Off()
        
    def Get_Current_Mode(self):
        '''
        "Mute" if in mute mode. "Gate" if in gate mode.
        '''
        return self.Mode.Current_State_Name()
    
class Send(object):
    '''
    Send object for the effects loop of the noise gate.  This is what will attach to other input devices.
    '''
    
    def __init__(self):
        pass
