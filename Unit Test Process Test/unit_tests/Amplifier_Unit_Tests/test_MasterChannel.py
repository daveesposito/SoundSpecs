'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.MasterChannel import MasterChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Master = MasterChannel()
        self.assertEqual(Master.Volume.Current_Position(), 0.0, "Failed to initialize Volume.")
        self.assertEqual(Master.Reverb.Current_Position(), 0.0, "Failed to initialize Reverb.")
        self.assertEqual(Master.Send_Level.Current_Position(), 0.0, "Failed to initialize Send Level.")

    def testConstructorWithVolumeSetting(self):
        Master = MasterChannel(volume=4)
        self.assertEqual(Master.Volume.Current_Position(), 4, "Failed to initialize Volume.")

    def testConstructorWithReverbSetting(self):
        Master = MasterChannel(reverb=5.1)
        self.assertEqual(Master.Reverb.Current_Position(), 5.1, "Failed to initialize Reverb.")
    
    def testConstructorWithSendLevelSetting(self):
        Master = MasterChannel(send_level=9.9)
        self.assertEqual(Master.Send_Level.Current_Position(), 9.9, "Failed to initialize Send Level.")
        
    def testConstructorWithAllSettings(self):
        Master = MasterChannel(3, 7, 9)
        self.assertEqual(Master.Volume.Current_Position(), 3.0, "Failed to initialize Volume.")
        self.assertEqual(Master.Reverb.Current_Position(), 7.0, "Failed to initialize Reverb.")
        self.assertEqual(Master.Send_Level.Current_Position(), 9.0, "Failed to initialize Send Level.")
    
    def testReadDefaultChannelSelection(self):
        Master = MasterChannel()
        self.assertEqual(Master.Current_Type(), "Clean", "Failed to correctly initialize channel selector.") 
    
    def testSelectCrunch(self):
        Master = MasterChannel()
        Master.Select_Drive()
        self.assertEqual(Master.Current_Type(), "Drive", "Failed to set to Drive.")  
    
    def testSelectClean(self):
        Master = MasterChannel()
        Master.Select_Drive()
        self.assertEqual(Master.Current_Type(), "Drive", "Failed to set to Drive.")
        Master.Select_Clean()
        self.assertEqual(Master.Current_Type(), "Clean", "Failed to set to Clean.") 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()