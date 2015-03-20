'''
Created on Mar 18, 2015

@author: desposito
'''
from Utilities.Controls import Switch, Knob

class Focusrite_Saffire_Pro40(object):
    '''
    Simulates input / output channels of the Focusrite Saffire Pro40 audio interface.
    '''

    def __init__(self, main_level=0.0, mic_level_1=0.0, mic_level_2=0.0):
        '''
        Constructor
        '''
        self.AnalogInputs = list()
        self.AnalogOutputs = list()
        self.PhantomPower = list()
        self.MicLevels = list()
        for n in range(8):
            self.AnalogInputs.append(InputChannel())
            self.AnalogOutputs.append(OutputChannel())
            if n == 0 or n == 1:
                self.AnalogInputs[n].Assign_Switches()
        self.PhantomPower.append(Switch("Bank 1 Phantom Power", current_state=False))
        self.PhantomPower.append(Switch("Bank 2 Phantom Power", current_state=False))
        self.MainLevel = Knob("Main Level", current_position=main_level)
        self.MicLevels.append(Knob("Mic 1 Level", current_position=mic_level_1))
        self.MicLevels.append(Knob("Mic 2 Level", current_position=mic_level_2))
        
    def _Get_Switch_Based_On_Channel(self, channel):
        '''
        Returns the first switch object if channels are 1-4
        Returns the second switch object if channels are 5-8
        '''
        if channel in [1,2,3,4]:
            return self.PhantomPower[0]
        elif channel in [5,6,7,8]:
            return self.PhantomPower[1]
        else:
            raise ValueError("Invalid channel provided.")
        
    def IsChannelUsingPhantomPower(self, channel):
        '''
        For the given channel, returns true if phantom power is on, false if phantom power is off.
        '''
        return self._Get_Switch_Based_On_Channel(channel).Current_State()
        
class OutputChannel(object):
    '''
    Abstraction of a single output channel on the FSP40.
    '''
    
    def __init__(self, level=0.0):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)

class InputChannel(object):
    '''
    Abstraction of a single input channel on the FSP40.
    '''
    
    def __init__(self, level=0.0, connected_device=None):
        '''
        Constructor
        '''
        self.Level = Knob("Level", current_position=level)
        self.ConnectedDevice = connected_device
        self.InstrumentSwitch = None
        self.PadSwitch = None
        
    def Assign_Switches(self):
        '''
        Channels 1 and 2 have additional level controls.  This will assign these.
        '''
        self.InstrumentSwitch = Switch("Instrument Level", current_state=False)
        self.PadSwitch = Switch("Pad", current_state=False)
        
    def Turn_Instrument_Level_On(self):
        '''
        Sets the channel to accept Instrument Level input.
        '''
        try:
            self.InstrumentSwitch.Turn_On()
        except:
            raise TypeError("This channel doesn't have an Instrument Level switch.")
        
    def Turn_Instrument_Level_Off(self):
        '''
        Sets the channel to accept mic level input.
        '''
        try:
            self.InstrumentSwitch.Turn_Off()
        except:
            raise TypeError("This channel doesn't have an Instrument Level switch.")
        
    def Turn_Pad_On(self):
        '''
        Activate pad to allow input levels of +16dBu.
        '''
        try:
            self.PadSwitch.Turn_On()
        except:
            raise TypeError("This channel doesn't have a Pad switch.")
        
    def Turn_Pad_Off(self):
        '''
        Deactivate pad to allow input levels of +7dBu.
        '''
        try:
            self.PadSwitch.Turn_Off()
        except:
            raise TypeError("This channel doesn't have a Pad switch.")
        
    def Is_Instrument_Switch_On(self):
        '''
        True if switch is On. False if switch is Off.
        '''
        if self.InstrumentSwitch.Current_State():
            return True
        else:
            return False
        
    def Is_Pad_Switch_On(self):
        '''
        True if switch is On. False if switch is Off.
        '''
        if self.PadSwitch.Current_State():
            return True
        else:
            return False