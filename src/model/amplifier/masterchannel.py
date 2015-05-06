'''
Created on Mar 13, 2015

@author: desposito
'''

from model.Utilities.Controls import Knob, Switch


class MasterChannel():
    '''Defines controls in the master channel of the Marshall G80RCD amp.
    '''


    def __init__(self, volume=0.0, reverb=0.0, send_level=0.0):
        '''
        Constructor
        '''

        try:
            volume_val = float(volume)
        except:
            raise TypeError("Invalid volume value: {0}".format(str(volume)))
        
        try:
            reverb_val = float(reverb)
        except:
            raise TypeError("Invalid reverb value: {0}".format(str(reverb)))
        
        try:
            send_level_val = float(send_level)
        except:
            raise TypeError("Invalid send_level value: {0}"\
                            .format(str(send_level)))
                    
        self.channel_select = Switch("Channel Select", "Clean", "Drive")
        self.volume = Knob("Master Volume", current_position=volume_val)
        self.reverb = Knob("Reverb", current_position=reverb_val)
        self.send_level = Knob("Send Level", current_position=send_level_val)
        
    def select_drive(self):
        '''Sets the amp to use the drive channel.
        '''
        
        self.channel_select.Turn_Off()
        
    def select_clean(self):
        '''Sets the amp to use the clean channel.
        '''
        
        self.channel_select.Turn_On()
        
    def current_type(self):
        '''Determines which channel the amp is using.
        '''
        
        return self.channel_select.Current_State_Name()
    