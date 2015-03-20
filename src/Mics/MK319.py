'''
Created on Mar 18, 2015

@author: desposito
'''
from Mics.Mic import Mic
from Utilities.Controls import Switch

class MK319(Mic):
    '''
    Models the switches on the MK319 condenser mic based on the generic mic model.
    '''

    def __init__(self, name, high_pass=False, pad=False):
        '''
        Constructor
        '''
        Mic.__init__(self, name)
        self.HighPass = Switch("High Pass", current_state=high_pass)
        self.Pad = Switch("Pad", current_state=pad)
        
    def Turn_High_Pass_On(self):
        '''
        Turn on highpass filter.
        '''
        self.HighPass.Turn_On()
        
    def Turn_High_Pass_Off(self):
        '''
        Turn off highpass filter.
        '''
        self.HighPass.Turn_Off()
        
    def Turn_Pad_On(self):
        '''
        Turn on pad circuit.
        '''
        self.Pad.Turn_On()
        
    def Turn_Pad_Off(self):
        '''
        Turn off pad circuit.
        '''
        self.Pad.Turn_Off()
        
    def Is_High_Pass_On(self):
        '''
        True if highpass is on.  False if highpass is off.
        '''
        if self.HighPass.Current_State():
            return True
        else:
            return False
        
    def Is_Pad_On(self):
        '''
        True if pad circuit is on.  False if pad circuit is off.
        '''
        if self.Pad.Current_State():
            return True
        else:
            return False