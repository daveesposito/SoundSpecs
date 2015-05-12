'''
Created on Mar 19, 2015

@author: desposito
'''
import unittest
from model.interfaces.imp2 import IMP2

class Test(unittest.TestCase):

    def test_ValidateDefaultContructor(self):
        dibox = IMP2()
        self.assertEqual(dibox.level.current_position, 10.0)
        self.assertIsNone(dibox.connected_device.device)

    def test_ConstructorWithLevel(self):
        dibox = IMP2(level=9)
        self.assertEqual(dibox.level.current_position, 9)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultContructor']
    unittest.main()