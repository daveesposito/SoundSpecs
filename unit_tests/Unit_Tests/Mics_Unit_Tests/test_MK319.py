'''
Created on Mar 18, 2015

@author: desposito
'''
import unittest
from Mics.MK319 import MK319
from Mics.SM57 import SM57

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        M1 = MK319("MK319")
        self.assertEqual(M1.Name, "MK319")
        self.assertFalse(M1.HighPass.Current_State())
        self.assertFalse(M1.Pad.Current_State())
        
    def test_ConstructorWithHighPass(self):
        M1 = MK319("MK319", high_pass=True)
        self.assertTrue(M1.HighPass.Current_State())

    def test_ConstructorWithPad(self):
        M1 = MK319("MK319", pad=True)
        self.assertTrue(M1.Pad.Current_State())
        
    def test_SeparateInheritedMicsUseSameNamesInstance(self):
        M1 = MK319("MK319")
        M2 = SM57("SM57")
        self.assertEqual(M1.names, M2.names)
        
    def test_TurnHighPassOn(self):
        M1 = MK319("MK319")
        self.assertFalse(M1.HighPass.Current_State())
        M1.Turn_High_Pass_On()
        self.assertTrue(M1.HighPass.Current_State())
        
    def test_TurnHighPassOff(self):
        M1 = MK319("MK319", high_pass=True)
        self.assertTrue(M1.HighPass.Current_State())
        M1.Turn_High_Pass_Off()
        self.assertFalse(M1.HighPass.Current_State())
        
    def test_TurnPadOn(self):
        M1 = MK319("MK319")
        self.assertFalse(M1.Pad.Current_State())
        M1.Turn_Pad_On()
        self.assertTrue(M1.Pad.Current_State())
        
    def test_TurnPadOff(self):
        M1 = MK319("MK319", pad=True)
        self.assertTrue(M1.Pad.Current_State())
        M1.Turn_Pad_Off()
        self.assertFalse(M1.Pad.Current_State())

    def test_IsHighPassOnWhenSwitchedOn(self):
        M1 = MK319("MK319", high_pass=True)
        self.assertTrue(M1.Is_High_Pass_On())
        
    def test_IsHighPassOnWhenSwitchedOff(self):
        M1 = MK319("MK319")
        self.assertFalse(M1.Is_High_Pass_On())
        
    def test_IsPadOnWhenSwitchedOn(self):
        M1 = MK319("MK319", pad=True)
        self.assertTrue(M1.Is_Pad_On())
        
    def test_IsPadOnWhenSwitchedOff(self):
        M1 = MK319("MK319")
        self.assertFalse(M1.Is_Pad_On())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()