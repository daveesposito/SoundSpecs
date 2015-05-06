'''
Created on Mar 13, 2015

@author: desposito
'''

from cleanchannel import CleanChannel
from drivechannel import DriveChannel
from masterchannel import MasterChannel
from model.Utilities.Connection import Connection


class Amplifier(object):
    '''Models the controls on the Marshall G80RCD for storing signal chain 
       settings.
    '''

    
    def __init__(self):
        '''Creates all channels for this amp.
        
           connected_device should be assigned to the object that is connected 
           at the input of the amp.
        '''
        
        self.clean = CleanChannel()
        self.drive = DriveChannel()
        self.master = MasterChannel()
        self.connected_device = Connection()
        
    def set_clean_channel(self, gain=None, bass=None, mid=None, treble=None):
        '''Allows setting of any of the clean channel settings. These can also 
           be set individually via child objects.
        '''
        
        if gain is not None:
            self.clean.gain.Turn_To(gain)
        if bass is not None:
            self.clean.bass.Turn_To(bass)
        if mid is not None:
            self.clean.mid.Turn_To(mid)
        if treble is not None:
            self.clean.treble.Turn_To(treble)
        
    def set_drive_channel(self, gain=None, bass=None, mid=None, 
                          treble=None, contour=None, volume=None):
        '''Allows setting of any of the drive channel settings. These can also 
           be set individually via child objects.
        '''
        
        if gain is not None:
            self.drive.gain.Turn_To(gain)
        if bass is not None:
            self.drive.bass.Turn_To(bass)
        if mid is not None:
            self.drive.mid.Turn_To(mid)
        if treble is not None:
            self.drive.treble.Turn_To(treble)
        if contour is not None:
            self.drive.contour.Turn_To(contour)
        if volume is not None:
            self.drive.volume.Turn_To(volume)
            
    def set_master_channel(self, volume=None, reverb=None, send_level=None):
        '''Allows setting of any of the master channel settings. These can also
           be set individually via child objects.
        '''
        
        if volume is not None:
            self.master.volume.Turn_To(volume)
        if reverb is not None:
            self.master.reverb.Turn_To(reverb)
        if send_level is not None:
            self.master.send_level.Turn_To(send_level)