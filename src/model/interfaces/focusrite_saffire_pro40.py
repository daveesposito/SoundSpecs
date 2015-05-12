'''
Created on Mar 18, 2015

@author: desposito
'''

from model.utilities.controls import Switch, Knob
from model.utilities.connection import Connection


class Focusrite_Saffire_Pro40():
    '''Simulates input / output channels of the Focusrite Saffire Pro40 audio 
       interface.
    '''


    def __init__(self, main_level=0.0, phones_level_1=0.0, phones_level_2=0.0):
        '''
        Constructor
        '''
        
        self.a_ins = list()
        self.a_outs = list()
        self.phantom = list()
        self.phones_levels = list()
        
        for n in range(8):
            self.a_ins.append(InputChannel())
            self.a_outs.append(OutputChannel())
            if n == 0 or n == 1:
                self.a_ins[n]._assign_switches()
        
        self.main_level = Knob("Main Level", current_position=main_level)        
        self.phantom.append(Switch("Bank 1 Phantom Power", 
                                   state=False))
        self.phantom.append(Switch("Bank 2 Phantom Power", 
                                   state=False))
        self.phones_levels.append(Knob("Phones 1 Level", 
                                       current_position=phones_level_1))
        self.phones_levels.append(Knob("Phones 2 Level", 
                                       current_position=phones_level_2))
        
    def _get_switch_based_on_channel(self, channel):
        '''Returns the first switch object if channels are 1-4
           Returns the second switch object if channels are 5-8
        '''
        
        if channel in [1,2,3,4]:
            return self.phantom[0]
        elif channel in [5,6,7,8]:
            return self.phantom[1]
        else:
            raise ValueError("Invalid channel provided.")
        
    def is_channel_using_phantom_power(self, channel):
        '''For the given channel, returns true if phantom power is on, false 
           if phantom power is off.
        '''
        
        return self._get_switch_based_on_channel(channel).state
        
        
class OutputChannel():
    '''Abstraction of a single output channel on the FSP40.
    '''
    
    
    def __init__(self, level=0.0):
        '''Constructor
        '''
        
        self.level = Knob("Level", current_position=level)
        

class InputChannel():
    '''Abstraction of a single input channel on the FSP40.
    '''
    
    
    def __init__(self, level=0.0):
        '''Constructor
        '''
        
        self.level = Knob("Level", current_position=level)
        self.connected_device = Connection()
        self.inst_sw = None
        self.pad_sw = None
        
    def _assign_switches(self):
        '''Channels 1 and 2 have additional level controls.  This will assign 
           these.
        '''
        
        self.inst_sw = Switch("Instrument Level", state=False)
        self.pad_sw = Switch("Pad", state=False)
        
    def turn_instrument_level_on(self):
        '''Sets the channel to accept Instrument Level input.
        '''
        
        try:
            self.inst_sw.turn_on()
        except:
            raise TypeError("Channel doesn't have an Instrument Level switch.")
        
    def turn_instrument_level_off(self):
        '''Sets the channel to accept mic level input.
        '''
        
        try:
            self.inst_sw.turn_off()
        except:
            raise TypeError("Channel doesn't have an Instrument Level switch.")
        
    def turn_pad_on(self):
        '''Activate pad to allow input levels of +16dBu.
        '''
        
        try:
            self.pad_sw.turn_on()
        except:
            raise TypeError("Channel doesn't have a Pad switch.")
        
    def turn_pad_off(self):
        '''Deactivate pad to allow input levels of +7dBu.
        '''
        
        try:
            self.pad_sw.turn_off()
        except:
            raise TypeError("Channel doesn't have a Pad switch.")
        
    