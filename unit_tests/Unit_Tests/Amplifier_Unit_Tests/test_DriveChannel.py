'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.DriveChannel import DriveChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Drive = DriveChannel()
        self.assertEqual(Drive.Gain.Current_Position(), 0.0, "Failed to initialize Gain.")
        self.assertEqual(Drive.Bass.Current_Position(), 0.0, "Failed to initialize Bass.")
        self.assertEqual(Drive.Mid.Current_Position(), 0.0, "Failed to initialize Mid.")
        self.assertEqual(Drive.Treble.Current_Position(), 0.0, "Failed to initialize Treble.")
        self.assertEqual(Drive.Contour.Current_Position(), 0.0, "Failed to initialize Contour.")
        self.assertEqual(Drive.Volume.Current_Position(), 0.0, "Failed to initialize Volume.")

    def testConstructorWithGainSetting(self):
        Drive = DriveChannel(gain=4)
        self.assertEqual(Drive.Gain.Current_Position(), 4, "Failed to initialize Gain.")

    def testConstructorWithBassSetting(self):
        Drive = DriveChannel(bass=5.1)
        self.assertEqual(Drive.Bass.Current_Position(), 5.1, "Failed to initialize Bass.")
    
    def testConstructorWithMidSetting(self):
        Drive = DriveChannel(mid=7.3)
        self.assertEqual(Drive.Mid.Current_Position(), 7.3, "Failed to initialize Mid.")
    
    def testConstructorWithTrebleSetting(self):
        Drive = DriveChannel(treble=9.9)
        self.assertEqual(Drive.Treble.Current_Position(), 9.9, "Failed to initialize Treble.")
        
    def testConstructorWithContourSetting(self):
        Drive = DriveChannel(contour=9)
        self.assertEqual(Drive.Contour.Current_Position(), 9.0, "Failed to initialize Contour.")
        
    def testConstructorWithVolumeSetting(self):
        Drive = DriveChannel(volume=4)
        self.assertEqual(Drive.Volume.Current_Position(), 4, "Failed to initialize Volume.")
        
    def testConstructorWithAllSettings(self):
        Drive = DriveChannel(8, 7, 3, 6, 5, 4)
        self.assertEqual(Drive.Gain.Current_Position(), 8.0, "Failed to initialize Gain.")
        self.assertEqual(Drive.Bass.Current_Position(), 7.0, "Failed to initialize Bass.")
        self.assertEqual(Drive.Mid.Current_Position(), 3.0, "Failed to initialize Mid.")
        self.assertEqual(Drive.Treble.Current_Position(), 6.0, "Failed to initialize Treble.")
        self.assertEqual(Drive.Contour.Current_Position(), 5, "Failed to initialize Contour.")
        self.assertEqual(Drive.Volume.Current_Position(), 4, "Failed to initialize Volume.")
    
    def testReadDefaultDriveType(self):
        Drive = DriveChannel()
        self.assertEqual(Drive.Current_Type(), "OD1", "Failed to correctly initialize drive type.") 
    
    def testSelectOD2(self):
        Drive = DriveChannel()
        Drive.Select_OD2()
        self.assertEqual(Drive.Current_Type(), "OD2", "Failed to set to OD2.")  
    
    def testSelectOD1(self):
        Drive = DriveChannel()
        Drive.Select_OD2()
        self.assertEqual(Drive.Current_Type(), "OD2", "Failed to set to OD2.")
        Drive.Select_OD1()
        self.assertEqual(Drive.Current_Type(), "OD1", "Failed to set to OD1.") 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()