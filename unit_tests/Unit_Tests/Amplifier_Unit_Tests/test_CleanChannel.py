'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from model.amplifier.cleanchannel import CleanChannel

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        clean = CleanChannel()
        self.assertEqual(clean.gain.Current_Position(), 0.0)
        self.assertEqual(clean.bass.Current_Position(), 0.0)
        self.assertEqual(clean.mid.Current_Position(), 0.0)
        self.assertEqual(clean.treble.Current_Position(), 0.0)

    def testConstructorWithGainSetting(self):
        clean = CleanChannel(gain=4)
        self.assertEqual(clean.gain.Current_Position(), 4)

    def testConstructorWithBassSetting(self):
        clean = CleanChannel(bass=5.1)
        self.assertEqual(clean.bass.Current_Position(), 5.1)
        
    def testConstructorWithMidSetting(self):
        clean = CleanChannel(mid=4.7)
        self.assertEqual(clean.mid.Current_Position(), 4.7)
    
    def testConstructorWithTrebleSetting(self):
        clean = CleanChannel(treble=9.9)
        self.assertEqual(clean.treble.Current_Position(), 9.9)
        
    def testConstructorWithAllSettings(self):
        clean = CleanChannel(3, 7, 8, 9)
        self.assertEqual(clean.gain.Current_Position(), 3.0)
        self.assertEqual(clean.bass.Current_Position(), 7.0)
        self.assertEqual(clean.mid.Current_Position(), 8.0)
        self.assertEqual(clean.treble.Current_Position(), 9.0)
    
    def testReadDefaultCleanType(self):
        clean = CleanChannel()
        self.assertEqual(clean.current_type(), "Clean") 
    
    def testSelectCrunch(self):
        clean = CleanChannel()
        clean.select_crunch()
        self.assertEqual(clean.current_type(), "Crunch")  
    
    def testSelectClean(self):
        clean = CleanChannel()
        clean.select_crunch()
        self.assertEqual(clean.current_type(), "Crunch")
        clean.select_clean()
        self.assertEqual(clean.current_type(), "Clean")    
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()