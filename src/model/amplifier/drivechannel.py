'''
Created on Mar 12, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Switch


class DriveChannel():
    '''Defines controls in the drive channel of the Marshall G80RCD amp.
    '''


    def __init__(self, gain=0.0, bass=0.0, mid=0.0, treble=0.0, 
                 contour=0.0, volume=0.0):
        '''Constructor
        '''
        
        try:
            gain_val = float(gain)
        except:
            raise TypeError("Invalid gain value: {0}".format(str(gain)))
        
        try:
            bass_val = float(bass)
        except:
            raise TypeError("Invalid bass value: {0}".format(str(bass)))
        
        try:
            mid_val = float(mid)
        except:
            raise TypeError("Invalid mid value: {0}".format(str(mid)))
        
        try:
            treble_val = float(treble)
        except:
            raise TypeError("Invalid treble value: {0}".format(str(treble)))
                    
        try:
            contour_val = float(contour)
        except:
            raise TypeError("Invalid contour value: {0}".format(str(contour)))
        
        try:
            volume_val = float(volume)
        except:
            raise TypeError("Invalid volume value: {0}".format(str(volume)))
        
        self.drive_type = Switch("Drive Type", "OD2", "OD1", False)
        self.gain = Knob("Gain", current_position=gain_val)
        self.bass = Knob("Bass", current_position=bass_val)
        self.mid = Knob("Mid", current_position=mid_val)
        self.treble = Knob("Treble", current_position=treble_val)
        self.contour = Knob("Contour", current_position=contour_val)
        self.volume = Knob("Volume", current_position=volume_val)
        
    def select_OD2(self):
        '''Activate Heavy Distortion.
        '''
        
        self.drive_type.turn_on()
        
    def select_OD1(self):
        '''Activate Crunchy Distortion.
        '''
        
        self.drive_type.turn_off()
        
    def current_type(self):
        '''Determines which circuit the drive channel is using.
        '''
        
        return self.drive_type.state_name()
    