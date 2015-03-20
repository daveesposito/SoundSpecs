'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.CleanChannel import CleanChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Clean = CleanChannel()
        self.assertEqual(Clean.Gain.Current_Position(), 0.0)
        self.assertEqual(Clean.Bass.Current_Position(), 0.0)
        self.assertEqual(Clean.Mid.Current_Position(), 0.0)
        self.assertEqual(Clean.Treble.Current_Position(), 0.0)

    def testConstructorWithGainSetting(self):
        Clean = CleanChannel(gain=4)
        self.assertEqual(Clean.Gain.Current_Position(), 4)

    def testConstructorWithBassSetting(self):
        Clean = CleanChannel(bass=5.1)
        self.assertEqual(Clean.Bass.Current_Position(), 5.1)
        
    def testConstructorWithMidSetting(self):
        Clean = CleanChannel(mid=4.7)
        self.assertEqual(Clean.Mid.Current_Position(), 4.7)
    
    def testConstructorWithTrebleSetting(self):
        Clean = CleanChannel(treble=9.9)
        self.assertEqual(Clean.Treble.Current_Position(), 9.9)
        
    def testConstructorWithAllSettings(self):
        Clean = CleanChannel(3, 7, 8, 9)
        self.assertEqual(Clean.Gain.Current_Position(), 3.0)
        self.assertEqual(Clean.Bass.Current_Position(), 7.0)
        self.assertEqual(Clean.Mid.Current_Position(), 8.0)
        self.assertEqual(Clean.Treble.Current_Position(), 9.0)
    
    def testReadDefaultCleanType(self):
        Clean = CleanChannel()
        self.assertEqual(Clean.Current_Type(), "Clean") 
    
    def testSelectCrunch(self):
        Clean = CleanChannel()
        Clean.Select_Crunch()
        self.assertEqual(Clean.Current_Type(), "Crunch")  
    
    def testSelectClean(self):
        Clean = CleanChannel()
        Clean.Select_Crunch()
        self.assertEqual(Clean.Current_Type(), "Crunch")
        Clean.Select_Clean()
        self.assertEqual(Clean.Current_Type(), "Clean")    
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()