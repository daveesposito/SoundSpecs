'''
Created on Mar 18, 2015

@author: desposito
'''

import unittest

from model.mics.mk319 import MK319
from model.mics.sm57 import SM57


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        mic = MK319("MK319")
        self.assertEqual(mic.name, "MK319")
        self.assertFalse(mic.high_pass.state)
        self.assertFalse(mic.pad.state)
        
    def test_ConstructorWithHighPass(self):
        mic = MK319("MK319", high_pass=True)
        self.assertTrue(mic.high_pass.state)

    def test_ConstructorWithPad(self):
        mic = MK319("MK319", pad=True)
        self.assertTrue(mic.pad.state)
        
    def test_SeparateInheritedMicsUseSameNamesInstance(self):
        mic1 = MK319("MK319")
        mic2 = SM57("sm57")
        self.assertEqual(mic1.names, mic2.names)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()
    
    