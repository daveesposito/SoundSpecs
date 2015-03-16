'''
Created on Mar 13, 2015

@author: desposito
'''
from Amplifier.Controls import Knob, Switch

class MasterChannel(object):
    '''
    classdocs
    '''

    def __init__(self, volume=0.0, reverb=0.0, send_level=0.0):
        '''
        Constructor
        '''
        try:
            volume_val = float(volume)
        except:
            raise TypeError("Invalid volume value: " + str(volume))
        
        try:
            reverb_val = float(reverb)
        except:
            raise TypeError("Invalid reverb value: " + str(reverb))
        
        try:
            send_level_val = float(send_level)
        except:
            raise TypeError("Invalid send_level value: " + str(send_level))
                    
        self.ChannelSelect = Switch("Channel Select", "Clean", "Drive")
        self.Volume = Knob("Master Volume", current_position=volume_val)
        self.Reverb = Knob("Reverb", current_position=reverb_val)
        self.Send_Level = Knob("Send Level", current_position=send_level_val)
        
    def Select_Drive(self):
        self.ChannelSelect.Turn_Off()
        
    def Select_Clean(self):
        self.ChannelSelect.Turn_On()
        
    def Current_Type(self):
        return self.ChannelSelect.Current_State_Name()