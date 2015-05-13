'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.amplifier.cleanchannel import CleanChannel


class Test(unittest.TestCase):


    def test_DefaultConstructorValidation(self):
        
        clean = CleanChannel()
        self.assertEqual(clean.gain.current_position, 0.0)
        self.assertEqual(clean.bass.current_position, 0.0)
        self.assertEqual(clean.mid.current_position, 0.0)
        self.assertEqual(clean.treble.current_position, 0.0)

    def test_ConstructorWithGainSetting(self):
        
        clean = CleanChannel(gain=4)
        self.assertEqual(clean.gain.current_position, 4)

    def test_ConstructorWithBassSetting(self):
        
        clean = CleanChannel(bass=5.1)
        self.assertEqual(clean.bass.current_position, 5.1)
        
    def test_ConstructorWithMidSetting(self):
        
        clean = CleanChannel(mid=4.7)
        self.assertEqual(clean.mid.current_position, 4.7)
    
    def test_ConstructorWithTrebleSetting(self):
        
        clean = CleanChannel(treble=9.9)
        self.assertEqual(clean.treble.current_position, 9.9)

    def test_NonNumbericGainRaisesException(self):
        
        self.assertRaises(TypeError, CleanChannel, gain="gain")
    
    def test_NonNumbericBassRaisesException(self):
        
        self.assertRaises(TypeError, CleanChannel, bass="bass")
        
    def test_NonNumbericMidRaisesException(self):
        
        self.assertRaises(TypeError, CleanChannel, mid="mid")
        
    def test_NonNumbericTrebleRaisesException(self):
        
        self.assertRaises(TypeError, CleanChannel, treble="treble")
        
    def test_ConstructorWithAllSettings(self):
        
        clean = CleanChannel(3, 7, 8, 9)
        self.assertEqual(clean.gain.current_position, 3.0)
        self.assertEqual(clean.bass.current_position, 7.0)
        self.assertEqual(clean.mid.current_position, 8.0)
        self.assertEqual(clean.treble.current_position, 9.0)
    
    def test_ReadDefaultCleanType(self):
        
        clean = CleanChannel()
        self.assertEqual(clean.current_type(), "Clean") 
    
    def test_SelectCrunch(self):
        
        clean = CleanChannel()
        clean.select_crunch()
        self.assertEqual(clean.current_type(), "Crunch")  
    
    def test_SelectClean(self):
        
        clean = CleanChannel()
        clean.select_crunch()
        self.assertEqual(clean.current_type(), "Crunch")
        clean.select_clean()
        self.assertEqual(clean.current_type(), "Clean")    
             
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    