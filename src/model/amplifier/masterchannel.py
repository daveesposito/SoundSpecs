'''
Created on Mar 13, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Switch


class MasterChannel():
    '''Defines controls in the master channel of the Marshall G80RCD amp.
    '''


    def __init__(self, volume=0.0, reverb=0.0, send_level=0.0):
        '''Constructor
        '''

        volume_val = self._is_value_float(volume)
        reverb_val = self._is_value_float(reverb)
        send_level_val = self._is_value_float(send_level)
                    
        self.channel_select = Switch("Channel Select", "Clean", "Drive")
        self.volume = Knob("Master Volume", current_position=volume_val)
        self.reverb = Knob("Reverb", current_position=reverb_val)
        self.send_level = Knob("Send Level", current_position=send_level_val)
        
    def select_drive(self):
        '''Sets the amp to use the drive channel.
        '''
        
        self.channel_select.turn_off()
        
    def select_clean(self):
        '''Sets the amp to use the clean channel.
        '''
        
        self.channel_select.turn_on()
        
    def current_type(self):
        '''Determines which channel the amp is using.
        '''
        
        return self.channel_select.state_name()
    
    def _is_value_float(self, value):
        '''Ensure that the provided value can be reprented as a float.
        '''
        
        try:
            return float(value)
        except:
            raise TypeError("Invalid input: {0}".format(value))
        