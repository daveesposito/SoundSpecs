'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Amplifier.CleanChannel import CleanChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Clean = CleanChannel()
        self.assertEqual(Clean.Gain.Current_Position(), 0.0, "Failed to initialize Gain.")
        self.assertEqual(Clean.Bass.Current_Position(), 0.0, "Failed to initialize Bass.")
        self.assertEqual(Clean.Treble.Current_Position(), 0.0, "Failed to initialize Treble.")

    def testConstructorWithGainSetting(self):
        Clean = CleanChannel(gain=4)
        self.assertEqual(Clean.Gain.Current_Position(), 4, "Failed to initialize Gain.")

    def testConstructorWithBassSetting(self):
        Clean = CleanChannel(bass=5.1)
        self.assertEqual(Clean.Bass.Current_Position(), 5.1, "Failed to initialize Bass.")
    
    def testConstructorWithTrebleSetting(self):
        Clean = CleanChannel(treble=9.9)
        self.assertEqual(Clean.Treble.Current_Position(), 9.9, "Failed to initialize Treble.")
        
    def testConstructorWithAllSettings(self):
        Clean = CleanChannel(3, 7, 9)
        self.assertEqual(Clean.Gain.Current_Position(), 3.0, "Failed to initialize Gain.")
        self.assertEqual(Clean.Bass.Current_Position(), 7.0, "Failed to initialize Bass.")
        self.assertEqual(Clean.Treble.Current_Position(), 9.0, "Failed to initialize Treble.")
    
    def testReadDefaultCleanType(self):
        Clean = CleanChannel()
        self.assertEqual(Clean.Current_Type(), "Clean", "Failed to correctly initialize clean type.") 
    
    def testSelectCrunch(self):
        Clean = CleanChannel()
        Clean.Select_Crunch()
        self.assertEqual(Clean.Current_Type(), "Crunch", "Failed to set to Crunch.")  
    
    def testSelectClean(self):
        Clean = CleanChannel()
        Clean.Select_Crunch()
        self.assertEqual(Clean.Current_Type(), "Crunch", "Failed to set to Crunch.")
        Clean.Select_Clean()
        self.assertEqual(Clean.Current_Type(), "Clean", "Failed to set to Clean.")    
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()