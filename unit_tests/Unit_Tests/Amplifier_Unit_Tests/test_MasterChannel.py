'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.MasterChannel import MasterChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Master = MasterChannel()
        self.assertEqual(Master.Volume.Current_Position(), 0.0)
        self.assertEqual(Master.Reverb.Current_Position(), 0.0)
        self.assertEqual(Master.Send_Level.Current_Position(), 0.0)

    def testConstructorWithVolumeSetting(self):
        Master = MasterChannel(volume=4)
        self.assertEqual(Master.Volume.Current_Position(), 4)

    def testConstructorWithReverbSetting(self):
        Master = MasterChannel(reverb=5.1)
        self.assertEqual(Master.Reverb.Current_Position(), 5.1)
    
    def testConstructorWithSendLevelSetting(self):
        Master = MasterChannel(send_level=9.9)
        self.assertEqual(Master.Send_Level.Current_Position(), 9.9)
        
    def testConstructorWithAllSettings(self):
        Master = MasterChannel(3, 7, 9)
        self.assertEqual(Master.Volume.Current_Position(), 3.0)
        self.assertEqual(Master.Reverb.Current_Position(), 7.0)
        self.assertEqual(Master.Send_Level.Current_Position(), 9.0)
    
    def testReadDefaultChannelSelection(self):
        Master = MasterChannel()
        self.assertEqual(Master.Current_Type(), "Clean") 
    
    def testSelectCrunch(self):
        Master = MasterChannel()
        Master.Select_Drive()
        self.assertEqual(Master.Current_Type(), "Drive")  
    
    def testSelectClean(self):
        Master = MasterChannel()
        Master.Select_Drive()
        self.assertEqual(Master.Current_Type(), "Drive")
        Master.Select_Clean()
        self.assertEqual(Master.Current_Type(), "Clean") 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()