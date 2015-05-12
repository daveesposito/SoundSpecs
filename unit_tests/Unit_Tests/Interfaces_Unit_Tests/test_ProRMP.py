'''
Created on Mar 27, 2015

@author: Dave
'''

import unittest

from model.interfaces.pro_rmp import ProRMP


class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        
        reamp = ProRMP()
        self.assertEqual(reamp.level.current_position, 10.0)
        self.assertFalse(reamp.lift.state)
        self.assertIsNone(reamp.connected_device.device)
        
    def test_ConstructorWithLevel(self):
        
        reamp = ProRMP(level=6)
        self.assertEqual(reamp.level.current_position, 6)
        
    def test_ConstructorWithLift(self):
        
        reamp = ProRMP(lift=True)
        self.assertTrue(reamp.lift.state)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()
    
    