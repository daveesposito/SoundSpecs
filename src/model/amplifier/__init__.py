'''
Created on Mar 13, 2015

@author: desposito
'''

from cleanchannel import CleanChannel
from drivechannel import DriveChannel
from masterchannel import MasterChannel
from model.utilities.connection import Connection


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
            self.clean.gain.turn_to(gain)
        if bass is not None:
            self.clean.bass.turn_to(bass)
        if mid is not None:
            self.clean.mid.turn_to(mid)
        if treble is not None:
            self.clean.treble.turn_to(treble)
        
    def set_drive_channel(self, gain=None, bass=None, mid=None, 
                          treble=None, contour=None, volume=None):
        '''Allows setting of any of the drive channel settings. These can also 
           be set individually via child objects.
        '''
        
        if gain is not None:
            self.drive.gain.turn_to(gain)
        if bass is not None:
            self.drive.bass.turn_to(bass)
        if mid is not None:
            self.drive.mid.turn_to(mid)
        if treble is not None:
            self.drive.treble.turn_to(treble)
        if contour is not None:
            self.drive.contour.turn_to(contour)
        if volume is not None:
            self.drive.volume.turn_to(volume)
            
    def set_master_channel(self, volume=None, reverb=None, send_level=None):
        '''Allows setting of any of the master channel settings. These can also
           be set individually via child objects.
        '''
        
        if volume is not None:
            self.master.volume.turn_to(volume)
        if reverb is not None:
            self.master.reverb.turn_to(reverb)
        if send_level is not None:
            self.master.send_level.turn_to(send_level)