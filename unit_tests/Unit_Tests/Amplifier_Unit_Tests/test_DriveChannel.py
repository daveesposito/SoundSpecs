'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.amplifier.drivechannel import DriveChannel


class Test(unittest.TestCase):


    def test_DefaultConstructorValidation(self):
        
        drive = DriveChannel()
        self.assertEqual(drive.gain.current_position, 0.0)
        self.assertEqual(drive.bass.current_position, 0.0)
        self.assertEqual(drive.mid.current_position, 0.0)
        self.assertEqual(drive.treble.current_position, 0.0)
        self.assertEqual(drive.contour.current_position, 0.0)
        self.assertEqual(drive.volume.current_position, 0.0)

    def test_ConstructorWithGainSetting(self):
        
        drive = DriveChannel(gain=4)
        self.assertEqual(drive.gain.current_position, 4)

    def test_ConstructorWithBassSetting(self):
        
        drive = DriveChannel(bass=5.1)
        self.assertEqual(drive.bass.current_position, 5.1)
    
    def test_ConstructorWithMidSetting(self):
        
        drive = DriveChannel(mid=7.3)
        self.assertEqual(drive.mid.current_position, 7.3)
    
    def test_ConstructorWithTrebleSetting(self):
        
        drive = DriveChannel(treble=9.9)
        self.assertEqual(drive.treble.current_position, 9.9)
        
    def test_ConstructorWithContourSetting(self):
        
        drive = DriveChannel(contour=9)
        self.assertEqual(drive.contour.current_position, 9.0)
        
    def test_ConstructorWithVolumeSetting(self):
        
        drive = DriveChannel(volume=4)
        self.assertEqual(drive.volume.current_position, 4)
        
    def test_NonNumbericGainRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, gain="gain")
        
    def test_NonNumbericBassRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, bass="bass")
        
    def test_NonNumbericMidRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, mid="mid")
        
    def test_NonNumbericTrebleRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, treble="treble")
        
    def test_NonNumbericContourRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, contour="contour")
        
    def test_NonNumbericVolumeRaisesException(self):
        
        self.assertRaises(TypeError, DriveChannel, volume="volume")
        
    def test_ConstructorWithAllSettings(self):
        
        drive = DriveChannel(8, 7, 3, 6, 5, 4)
        self.assertEqual(drive.gain.current_position, 8.0)
        self.assertEqual(drive.bass.current_position, 7.0)
        self.assertEqual(drive.mid.current_position, 3.0)
        self.assertEqual(drive.treble.current_position, 6.0)
        self.assertEqual(drive.contour.current_position, 5)
        self.assertEqual(drive.volume.current_position, 4)
    
    def test_ReadDefaultdriveType(self):
        
        drive = DriveChannel()
        self.assertEqual(drive.current_type(), "OD1") 
    
    def test_SelectOD2(self):
        
        drive = DriveChannel()
        drive.select_OD2()
        self.assertEqual(drive.current_type(), "OD2")  
    
    def test_SelectOD1(self):
        
        drive = DriveChannel()
        drive.select_OD2()
        self.assertEqual(drive.current_type(), "OD2")
        drive.select_OD1()
        self.assertEqual(drive.current_type(), "OD1") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    