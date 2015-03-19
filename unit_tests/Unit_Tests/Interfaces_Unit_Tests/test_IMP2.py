'''
Created on Mar 19, 2015

@author: desposito
'''
import unittest
from Interfaces.IMP2 import IMP2
from Pedals.Gate import Gate

class Test(unittest.TestCase):


    def test_ValidateDefaultContructor(self):
        I1 = IMP2()
        self.assertEqual(I1.Level.Current_Position(), 10.0, "Level not initialized.")
        self.assertIsNone(I1.ConnectedDevice, "Device connected somehow.")

    def test_ConstructorWithLevel(self):
        I1 = IMP2(level=9)
        self.assertEqual(I1.Level.Current_Position(), 9, "Level not set.")
        
    def test_ConstructorWithDevice(self):
        G1 = Gate()
        I1 = IMP2(connected_device=G1)
        self.assertIsInstance(I1.ConnectedDevice, Gate, "Didn't assign Gate.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultContructor']
    unittest.main()