'''
Created on Mar 19, 2015

@author: desposito
'''

import unittest

from model.amplifier import Amplifier
from model.amplifier.cleanchannel import CleanChannel
from model.amplifier.drivechannel import DriveChannel
from model.amplifier.masterchannel import MasterChannel


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        amp = Amplifier()
        self.assertIsNone(amp.connected_device.device)
        self.assertIsInstance(amp.clean, CleanChannel)
        self.assertIsInstance(amp.drive, DriveChannel)
        self.assertIsInstance(amp.master, MasterChannel)

    def test_SetCleanNone(self):
        
        amp = Amplifier()
        amp.set_clean_channel()
        self.assertEqual(amp.clean.gain.current_position, 0.0)
        self.assertEqual(amp.clean.bass.current_position, 0.0)
        self.assertEqual(amp.clean.mid.current_position, 0.0)
        self.assertEqual(amp.clean.treble.current_position, 0.0)
        
    def test_SetCleanGain(self):
        
        amp = Amplifier()
        amp.set_clean_channel(gain=4)
        self.assertEqual(amp.clean.gain.current_position, 4.0)
        self.assertEqual(amp.clean.bass.current_position, 0.0)
        self.assertEqual(amp.clean.mid.current_position, 0.0)
        self.assertEqual(amp.clean.treble.current_position, 0.0)
        
    def test_SetCleanBass(self):
        
        amp = Amplifier()
        amp.set_clean_channel(bass = 8)
        self.assertEqual(amp.clean.gain.current_position, 0.0)
        self.assertEqual(amp.clean.bass.current_position, 8.0)
        self.assertEqual(amp.clean.mid.current_position, 0.0)
        self.assertEqual(amp.clean.treble.current_position, 0.0)
    
    def test_SetCleanMid(self):
        
        amp = Amplifier()
        amp.set_clean_channel(mid=6.3)
        self.assertEqual(amp.clean.gain.current_position, 0.0)
        self.assertEqual(amp.clean.bass.current_position, 0.0)
        self.assertEqual(amp.clean.mid.current_position, 6.3)
        self.assertEqual(amp.clean.treble.current_position, 0.0)
        
    def test_SetCleanTreble(self):
        
        amp = Amplifier()
        amp.set_clean_channel(treble=9.9)
        self.assertEqual(amp.clean.gain.current_position, 0.0)
        self.assertEqual(amp.clean.bass.current_position, 0.0)
        self.assertEqual(amp.clean.mid.current_position, 0.0)
        self.assertEqual(amp.clean.treble.current_position, 9.9)
        
    def test_SetCleanAll(self):
        
        amp = Amplifier()
        amp.set_clean_channel(1, 2, 3, 4)
        self.assertEqual(amp.clean.gain.current_position, 1)
        self.assertEqual(amp.clean.bass.current_position, 2)
        self.assertEqual(amp.clean.mid.current_position, 3)
        self.assertEqual(amp.clean.treble.current_position, 4)
        
    def test_SetDriveNone(self):
        
        amp = Amplifier()
        amp.set_drive_channel()
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 0)
    
    def test_SetDriveGain(self):
        
        amp = Amplifier()
        amp.set_drive_channel(gain=1)
        self.assertEqual(amp.drive.gain.current_position, 1)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 0)
    
    def test_SetDriveBass(self):
        
        amp = Amplifier()
        amp.set_drive_channel(bass=2)
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 2)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 0)
    
    def test_SetDriveMid(self):
        
        amp = Amplifier()
        amp.set_drive_channel(mid=3)
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 3)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 0)
    
    def test_SetDriveTreble(self):
        
        amp = Amplifier()
        amp.set_drive_channel(treble=4)
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 4)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 0)
    
    def test_SetDriveContour(self):
        
        amp = Amplifier()
        amp.set_drive_channel(contour=5)
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 5)
        self.assertEqual(amp.drive.volume.current_position, 0)
        
    def test_SetDriveVolume(self):
        
        amp = Amplifier()
        amp.set_drive_channel(volume=6)
        self.assertEqual(amp.drive.gain.current_position, 0)
        self.assertEqual(amp.drive.bass.current_position, 0)
        self.assertEqual(amp.drive.mid.current_position, 0)
        self.assertEqual(amp.drive.treble.current_position, 0)
        self.assertEqual(amp.drive.contour.current_position, 0)
        self.assertEqual(amp.drive.volume.current_position, 6)
        
    def test_SetDriveAll(self):
        
        amp = Amplifier()
        amp.set_drive_channel(6, 5, 4, 3, 2, 1)
        self.assertEqual(amp.drive.gain.current_position, 6)
        self.assertEqual(amp.drive.bass.current_position, 5)
        self.assertEqual(amp.drive.mid.current_position, 4)
        self.assertEqual(amp.drive.treble.current_position, 3)
        self.assertEqual(amp.drive.contour.current_position, 2)
        self.assertEqual(amp.drive.volume.current_position, 1)
    
    def test_SetMasterNone(self):
        
        amp= Amplifier()
        amp.set_master_channel()
        self.assertEqual(amp.master.volume.current_position, 0)
        self.assertEqual(amp.master.reverb.current_position, 0)
        self.assertEqual(amp.master.send_level.current_position, 0)
        
    def test_SetMasterVolume(self):
        
        amp= Amplifier()
        amp.set_master_channel(volume=4)
        self.assertEqual(amp.master.volume.current_position, 4)
        self.assertEqual(amp.master.reverb.current_position, 0)
        self.assertEqual(amp.master.send_level.current_position, 0)
        
    def test_SetMasterReverb(self):
        
        amp= Amplifier()
        amp.set_master_channel(reverb=3)
        self.assertEqual(amp.master.volume.current_position, 0)
        self.assertEqual(amp.master.reverb.current_position, 3)
        self.assertEqual(amp.master.send_level.current_position, 0)
        
    def test_SetMasterSendLevel(self):
        
        amp= Amplifier()
        amp.set_master_channel(send_level=2)
        self.assertEqual(amp.master.volume.current_position, 0)
        self.assertEqual(amp.master.reverb.current_position, 0)
        self.assertEqual(amp.master.send_level.current_position, 2)
    
    def test_SetMasterAll(self):
        
        amp= Amplifier()
        amp.set_master_channel(1, 2, 3)
        self.assertEqual(amp.master.volume.current_position, 1)
        self.assertEqual(amp.master.reverb.current_position, 2)
        self.assertEqual(amp.master.send_level.current_position, 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()
    
    