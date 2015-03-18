'''
Created on Mar 18, 2015

@author: desposito
'''
import unittest
from Interfaces.Focusrite_Saffire_Pro40 import Focusrite_Saffire_Pro40

class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        F1 = Focusrite_Saffire_Pro40()
        self.assertEqual(len(F1.AnalogInputs), 8, "Analog Inputs not intiialized.")
        self.assertEqual(F1.AnalogInputs[0].Level, 0, "Level not set")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()