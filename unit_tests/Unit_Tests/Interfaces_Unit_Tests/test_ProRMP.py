'''
Created on Mar 27, 2015

@author: Dave
'''
import unittest
from model.Interfaces.ProRMP import ProRMP
from model.Interfaces.Focusrite_Saffire_Pro40 import Focusrite_Saffire_Pro40,\
    OutputChannel

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        R1 = ProRMP()
        self.assertEqual(R1.Level.Current_Position(), 10.0)
        self.assertFalse(R1.Lift.Current_State())
        self.assertIsNone(R1.ConnectedDevice)
        
    def test_ConstructorWithLevel(self):
        R1 = ProRMP(level=6)
        self.assertEqual(R1.Level.Current_Position(), 6)
        
    def test_ConstructorWithLift(self):
        R1 = ProRMP(lift=True)
        self.assertTrue(R1.Lift.Current_State())
        
    def test_ConstructorWithDevice(self):
        F1 = Focusrite_Saffire_Pro40()
        R1 = ProRMP(connected_device=F1.AnalogOutputs[2])
        self.assertIsInstance(R1.ConnectedDevice, OutputChannel)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()