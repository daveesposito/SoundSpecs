'''
Created on Mar 13, 2015

@author: desposito
'''
from CleanChannel import CleanChannel
from DriveChannel import DriveChannel
from MasterChannel import MasterChannel

class Amplifier(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.Clean = CleanChannel()
        self.Drive = DriveChannel()
        self.Master = MasterChannel()
        
    def Set_Clean_Channel(self, gain=None, bass=None, treble=None):
        if not gain is None:
            self.Clean.Gain.Turn_To(gain)
        if not bass is None:
            self.Clean.Bass.Turn_To(bass)
        if not treble is None:
            self.Clean.Treble.Turn_To(treble)
        
    def Set_Drive_Channel(self, gain=None, bass=None, mid=None, treble=None, contour=None, volume=None):
        if not gain is None:
            self.Drive.Gain.Turn_To(gain)
        if not bass is None:
            self.Drive.Bass.Turn_To(bass)
        if not mid is None:
            self.Drive.Mid.Turn_To(mid)
        if not treble is None:
            self.Drive.Treble.Turn_To(treble)
        if not contour is None:
            self.Drive.Contour.Turn_To(contour)
        if not volume is None:
            self.Drive.Volume.Turn_To(volume)
            
    def Set_Master_Channel(self, volume=None, reverb=None, send_level=None):
        if not volume is None:
            self.Master.Volume.Turn_To(volume)
        if not reverb is None:
            self.Master.Reverb.Turn_To(reverb)
        if not send_level is None:
            self.Master.Send_Level.Turn_To(send_level)
            
    