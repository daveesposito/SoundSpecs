'''
Created on Mar 19, 2015

@author: desposito
'''
import unittest
from model.Interfaces.IMP2 import IMP2

class Test(unittest.TestCase):

    def test_ValidateDefaultContructor(self):
        I1 = IMP2()
        self.assertEqual(I1.Level.Current_Position(), 10.0)
        self.assertIsNone(I1.ConnectedDevice.Device)

    def test_ConstructorWithLevel(self):
        I1 = IMP2(level=9)
        self.assertEqual(I1.Level.Current_Position(), 9)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultContructor']
    unittest.main()