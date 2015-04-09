'''
Created on Mar 27, 2015

@author: Dave
'''
import unittest
from model.Interfaces.ProRMP import ProRMP

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        R1 = ProRMP()
        self.assertEqual(R1.Level.Current_Position(), 10.0)
        self.assertFalse(R1.Lift.Current_State())
        self.assertIsNone(R1.ConnectedDevice.Device)
        
    def test_ConstructorWithLevel(self):
        R1 = ProRMP(level=6)
        self.assertEqual(R1.Level.Current_Position(), 6)
        
    def test_ConstructorWithLift(self):
        R1 = ProRMP(lift=True)
        self.assertTrue(R1.Lift.Current_State())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()