'''
Created on Mar 12, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Switch

class DriveChannel(object):
    '''
    Defines controls in the drive channel of the Marshall G80RCD amp.
    '''

    def __init__(self, gain=0.0, bass=0.0, mid=0.0, treble=0.0, contour=0.0, volume=0.0):
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
            mid_val = float(mid)
        except:
            raise TypeError("Invalid mid value: " + str(mid))
        
        try:
            treble_val = float(treble)
        except:
            raise TypeError("Invalid treble value: " + str(treble))
                    
        try:
            contour_val = float(contour)
        except:
            raise TypeError("Invalid contour value: " + str(contour))
        
        try:
            volume_val = float(volume)
        except:
            raise TypeError("Invalid volume value: " + str(volume))
        
        self.DriveType = Switch("Drive Type", "OD2", "OD1", False)
        self.Gain = Knob("Gain", current_position=gain_val)
        self.Bass = Knob("Bass", current_position=bass_val)
        self.Mid = Knob("Mid", current_position=mid_val)
        self.Treble = Knob("Treble", current_position=treble_val)
        self.Contour = Knob("Contour", current_position=contour_val)
        self.Volume = Knob("Volume", current_position=volume_val)
        
    def Select_OD2(self):
        '''
        Set the channel to use the OD2 circuit.
        '''
        self.DriveType.Turn_On()
        
    def Select_OD1(self):
        '''
        Set the channel to use the OD1 circuit.
        '''
        self.DriveType.Turn_Off()
        
    def Current_Type(self):
        '''
        Determines which circuit the drive channel is using.
        '''
        return self.DriveType.Current_State_Name()