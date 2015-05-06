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
        A1 = Amplifier()
        self.assertIsNone(A1.connected_device.Device)
        self.assertIsInstance(A1.clean, CleanChannel)
        self.assertIsInstance(A1.drive, DriveChannel)
        self.assertIsInstance(A1.master, MasterChannel)

    def test_SetCleanNone(self):
        A1 = Amplifier()
        A1.set_clean_channel()
        self.assertEqual(A1.clean.gain.Current_Position(), 0.0)
        self.assertEqual(A1.clean.bass.Current_Position(), 0.0)
        self.assertEqual(A1.clean.mid.Current_Position(), 0.0)
        self.assertEqual(A1.clean.treble.Current_Position(), 0.0)
        
    def test_SetCleanGain(self):
        A1 = Amplifier()
        A1.set_clean_channel(gain=4)
        self.assertEqual(A1.clean.gain.Current_Position(), 4.0)
        self.assertEqual(A1.clean.bass.Current_Position(), 0.0)
        self.assertEqual(A1.clean.mid.Current_Position(), 0.0)
        self.assertEqual(A1.clean.treble.Current_Position(), 0.0)
        
    def test_SetCleanBass(self):
        A1 = Amplifier()
        A1.set_clean_channel(bass = 8)
        self.assertEqual(A1.clean.gain.Current_Position(), 0.0)
        self.assertEqual(A1.clean.bass.Current_Position(), 8.0)
        self.assertEqual(A1.clean.mid.Current_Position(), 0.0)
        self.assertEqual(A1.clean.treble.Current_Position(), 0.0)
    
    def test_SetCleanMid(self):
        A1 = Amplifier()
        A1.set_clean_channel(mid=6.3)
        self.assertEqual(A1.clean.gain.Current_Position(), 0.0)
        self.assertEqual(A1.clean.bass.Current_Position(), 0.0)
        self.assertEqual(A1.clean.mid.Current_Position(), 6.3)
        self.assertEqual(A1.clean.treble.Current_Position(), 0.0)
        
    def test_SetCleanTreble(self):
        A1 = Amplifier()
        A1.set_clean_channel(treble=9.9)
        self.assertEqual(A1.clean.gain.Current_Position(), 0.0)
        self.assertEqual(A1.clean.bass.Current_Position(), 0.0)
        self.assertEqual(A1.clean.mid.Current_Position(), 0.0)
        self.assertEqual(A1.clean.treble.Current_Position(), 9.9)
        
    def test_SetCleanAll(self):
        A1 = Amplifier()
        A1.set_clean_channel(1, 2, 3, 4)
        self.assertEqual(A1.clean.gain.Current_Position(), 1)
        self.assertEqual(A1.clean.bass.Current_Position(), 2)
        self.assertEqual(A1.clean.mid.Current_Position(), 3)
        self.assertEqual(A1.clean.treble.Current_Position(), 4)
        
    def test_SetDriveNone(self):
        A1 = Amplifier()
        A1.set_drive_channel()
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
    
    def test_SetDriveGain(self):
        A1 = Amplifier()
        A1.set_drive_channel(gain=1)
        self.assertEqual(A1.drive.gain.Current_Position(), 1)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
    
    def test_SetDriveBass(self):
        A1 = Amplifier()
        A1.set_drive_channel(bass=2)
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 2)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
    
    def test_SetDriveMid(self):
        A1 = Amplifier()
        A1.set_drive_channel(mid=3)
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 3)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
    
    def test_SetDriveTreble(self):
        A1 = Amplifier()
        A1.set_drive_channel(treble=4)
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 4)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
    
    def test_SetDriveContour(self):
        A1 = Amplifier()
        A1.set_drive_channel(contour=5)
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 5)
        self.assertEqual(A1.drive.volume.Current_Position(), 0)
        
    def test_SetDriveVolume(self):
        A1 = Amplifier()
        A1.set_drive_channel(volume=6)
        self.assertEqual(A1.drive.gain.Current_Position(), 0)
        self.assertEqual(A1.drive.bass.Current_Position(), 0)
        self.assertEqual(A1.drive.mid.Current_Position(), 0)
        self.assertEqual(A1.drive.treble.Current_Position(), 0)
        self.assertEqual(A1.drive.contour.Current_Position(), 0)
        self.assertEqual(A1.drive.volume.Current_Position(), 6)
        
    def test_SetDriveAll(self):
        A1 = Amplifier()
        A1.set_drive_channel(6, 5, 4, 3, 2, 1)
        self.assertEqual(A1.drive.gain.Current_Position(), 6)
        self.assertEqual(A1.drive.bass.Current_Position(), 5)
        self.assertEqual(A1.drive.mid.Current_Position(), 4)
        self.assertEqual(A1.drive.treble.Current_Position(), 3)
        self.assertEqual(A1.drive.contour.Current_Position(), 2)
        self.assertEqual(A1.drive.volume.Current_Position(), 1)
    
    def test_SetMasterNone(self):
        A1= Amplifier()
        A1.set_master_channel()
        self.assertEqual(A1.master.volume.Current_Position(), 0)
        self.assertEqual(A1.master.reverb.Current_Position(), 0)
        self.assertEqual(A1.master.send_level.Current_Position(), 0)
        
    def test_SetMasterVolume(self):
        A1= Amplifier()
        A1.set_master_channel(volume=4)
        self.assertEqual(A1.master.volume.Current_Position(), 4)
        self.assertEqual(A1.master.reverb.Current_Position(), 0)
        self.assertEqual(A1.master.send_level.Current_Position(), 0)
        
    def test_SetMasterReverb(self):
        A1= Amplifier()
        A1.set_master_channel(reverb=3)
        self.assertEqual(A1.master.volume.Current_Position(), 0)
        self.assertEqual(A1.master.reverb.Current_Position(), 3)
        self.assertEqual(A1.master.send_level.Current_Position(), 0)
        
    def test_SetMasterSendLevel(self):
        A1= Amplifier()
        A1.set_master_channel(send_level=2)
        self.assertEqual(A1.master.volume.Current_Position(), 0)
        self.assertEqual(A1.master.reverb.Current_Position(), 0)
        self.assertEqual(A1.master.send_level.Current_Position(), 2)
    
    def test_SetMasterAll(self):
        A1= Amplifier()
        A1.set_master_channel(1, 2, 3)
        self.assertEqual(A1.master.volume.Current_Position(), 1)
        self.assertEqual(A1.master.reverb.Current_Position(), 2)
        self.assertEqual(A1.master.send_level.Current_Position(), 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()
    
    