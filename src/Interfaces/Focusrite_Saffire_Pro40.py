'''
Created on Mar 18, 2015

@author: desposito
'''
from Utilities.Controls import Switch, Knob

class Focusrite_Saffire_Pro40(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.AnalogInputs = list()
        self.PhantomPower = list()
        for n in range(8):
            self.AnalogInputs.append(InputChannel())
            if n == 0 or n == 1:
                self.AnalogInputs[n].Assign_Switches()
        self.PhantomPower.append(Switch("Bank 1 Phantom Power", current_state=False))
        self.PhantomPower.append(Switch("Bank 2 Phantom Power", current_state=False))
        
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
        
class InputChannel(object):
    '''
    classdocs
    '''
    
    def __init__(self, level=0.0, connected_device=None):
        '''
        constructor
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