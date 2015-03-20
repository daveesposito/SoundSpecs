'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.DriveChannel import DriveChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Drive = DriveChannel()
        self.assertEqual(Drive.Gain.Current_Position(), 0.0)
        self.assertEqual(Drive.Bass.Current_Position(), 0.0)
        self.assertEqual(Drive.Mid.Current_Position(), 0.0)
        self.assertEqual(Drive.Treble.Current_Position(), 0.0)
        self.assertEqual(Drive.Contour.Current_Position(), 0.0)
        self.assertEqual(Drive.Volume.Current_Position(), 0.0)

    def testConstructorWithGainSetting(self):
        Drive = DriveChannel(gain=4)
        self.assertEqual(Drive.Gain.Current_Position(), 4)

    def testConstructorWithBassSetting(self):
        Drive = DriveChannel(bass=5.1)
        self.assertEqual(Drive.Bass.Current_Position(), 5.1)
    
    def testConstructorWithMidSetting(self):
        Drive = DriveChannel(mid=7.3)
        self.assertEqual(Drive.Mid.Current_Position(), 7.3)
    
    def testConstructorWithTrebleSetting(self):
        Drive = DriveChannel(treble=9.9)
        self.assertEqual(Drive.Treble.Current_Position(), 9.9)
        
    def testConstructorWithContourSetting(self):
        Drive = DriveChannel(contour=9)
        self.assertEqual(Drive.Contour.Current_Position(), 9.0)
        
    def testConstructorWithVolumeSetting(self):
        Drive = DriveChannel(volume=4)
        self.assertEqual(Drive.Volume.Current_Position(), 4)
        
    def testConstructorWithAllSettings(self):
        Drive = DriveChannel(8, 7, 3, 6, 5, 4)
        self.assertEqual(Drive.Gain.Current_Position(), 8.0)
        self.assertEqual(Drive.Bass.Current_Position(), 7.0)
        self.assertEqual(Drive.Mid.Current_Position(), 3.0)
        self.assertEqual(Drive.Treble.Current_Position(), 6.0)
        self.assertEqual(Drive.Contour.Current_Position(), 5)
        self.assertEqual(Drive.Volume.Current_Position(), 4)
    
    def testReadDefaultDriveType(self):
        Drive = DriveChannel()
        self.assertEqual(Drive.Current_Type(), "OD1") 
    
    def testSelectOD2(self):
        Drive = DriveChannel()
        Drive.Select_OD2()
        self.assertEqual(Drive.Current_Type(), "OD2")  
    
    def testSelectOD1(self):
        Drive = DriveChannel()
        Drive.Select_OD2()
        self.assertEqual(Drive.Current_Type(), "OD2")
        Drive.Select_OD1()
        self.assertEqual(Drive.Current_Type(), "OD1") 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()