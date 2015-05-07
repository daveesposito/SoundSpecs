'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.amplifier.drivechannel import DriveChannel


class Test(unittest.TestCase):


    def testDefaultConstructorValidation(self):
        
        drive = DriveChannel()
        self.assertEqual(drive.gain.Current_Position(), 0.0)
        self.assertEqual(drive.bass.Current_Position(), 0.0)
        self.assertEqual(drive.mid.Current_Position(), 0.0)
        self.assertEqual(drive.treble.Current_Position(), 0.0)
        self.assertEqual(drive.contour.Current_Position(), 0.0)
        self.assertEqual(drive.volume.Current_Position(), 0.0)

    def testConstructorWithGainSetting(self):
        
        drive = DriveChannel(gain=4)
        self.assertEqual(drive.gain.Current_Position(), 4)

    def testConstructorWithBassSetting(self):
        
        drive = DriveChannel(bass=5.1)
        self.assertEqual(drive.bass.Current_Position(), 5.1)
    
    def testConstructorWithMidSetting(self):
        
        drive = DriveChannel(mid=7.3)
        self.assertEqual(drive.mid.Current_Position(), 7.3)
    
    def testConstructorWithTrebleSetting(self):
        
        drive = DriveChannel(treble=9.9)
        self.assertEqual(drive.treble.Current_Position(), 9.9)
        
    def testConstructorWithContourSetting(self):
        
        drive = DriveChannel(contour=9)
        self.assertEqual(drive.contour.Current_Position(), 9.0)
        
    def testConstructorWithVolumeSetting(self):
        
        drive = DriveChannel(volume=4)
        self.assertEqual(drive.volume.Current_Position(), 4)
        
    def testConstructorWithAllSettings(self):
        
        drive = DriveChannel(8, 7, 3, 6, 5, 4)
        self.assertEqual(drive.gain.Current_Position(), 8.0)
        self.assertEqual(drive.bass.Current_Position(), 7.0)
        self.assertEqual(drive.mid.Current_Position(), 3.0)
        self.assertEqual(drive.treble.Current_Position(), 6.0)
        self.assertEqual(drive.contour.Current_Position(), 5)
        self.assertEqual(drive.volume.Current_Position(), 4)
    
    def testReadDefaultdriveType(self):
        
        drive = DriveChannel()
        self.assertEqual(drive.current_type(), "OD1") 
    
    def testSelectOD2(self):
        
        drive = DriveChannel()
        drive.select_OD2()
        self.assertEqual(drive.current_type(), "OD2")  
    
    def testSelectOD1(self):
        
        drive = DriveChannel()
        drive.select_OD2()
        self.assertEqual(drive.current_type(), "OD2")
        drive.select_OD1()
        self.assertEqual(drive.current_type(), "OD1") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    