'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.Utilities.Controls import Knob


class Test(unittest.TestCase):


    def testDefaultConstructorValidation(self):
        
        volume = Knob("Volume")
        self.assertEqual(volume.name, "Volume")
        self.assertEqual(volume.min_value, 0.0)
        self.assertEqual(volume.max_value, 10.0)
        self.assertEqual(volume.current_position, 0.0)
        
    def test_ConstructorCannotTakePositionBelowMin(self):
        
        self.assertRaises(ValueError, Knob, "Volume", current_position=-1)
    
    def test_ConstructorCannotTakePositionAboveMax(self):
        self.assertRaises(ValueError, Knob, "Volume", current_position=11)
    
    def test_ValidatePositionRaisesExceptionIfPositionIsNotANumber(self):
        
        volume = Knob("Volume")
        self.assertRaises(TypeError, volume._validate_position, "knob")
    
    def test_ValidatePositionRaisesExceptionIfPositionIsBelowMin(self):
        
        volume = Knob("Volume")
        self.assertRaises(ValueError, volume._validate_position, -2)
    
    def test_ValidatePositionRaisesExceptionIfPositionIsAboveMax(self):
    
        volume = Knob("Volume")
        self.assertRaises(ValueError, volume._validate_position, 12)

    def test_TurnToWithValidValueSetsNewValue(self):

        volume = Knob("Volume")
        for setting in range(int(volume.max_value)+1):
            volume.turn_to(setting)
            self.assertEqual(volume.current_position, setting)
            
    def test_TurnToWithValidTooLargeRaisesException(self):
        
        volume = Knob("Volume")
        self.assertRaises(ValueError, volume.turn_to, 11)
        
    def test_TurnToWithValidTooSmallRaisesException(self):
        
        volume = Knob("Volume")
        self.assertRaises(ValueError, volume.turn_to, -1)

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    