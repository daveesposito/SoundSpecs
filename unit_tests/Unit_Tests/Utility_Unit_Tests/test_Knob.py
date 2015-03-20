'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Utilities.Controls import Knob

class Test(unittest.TestCase):

    def testDefaultConstructorValidation(self):
        Volume = Knob("Volume")
        self.assertEqual(Volume.Name, "Volume")
        self.assertEqual(Volume._min_value, 0.0)
        self.assertEqual(Volume._max_value, 10.0)
        self.assertEqual(Volume._current_position, 0.0)
        
    def test_ConstructorCannotTakePositionBelowMin(self):
        self.assertRaises(ValueError, Knob, "Volume", current_position=-1)
    
    def test_ConstructorCannotTakePositionAboveMax(self):
        self.assertRaises(ValueError, Knob, "Volume", current_position=11)
    
    def test_ValidatePositionRaisesExceptionIfPositionIsNotANumber(self):
        Volume = Knob("Volume")
        self.assertRaises(TypeError, Volume._validate_provided_position, "knob")
    
    def test_ValidatePositionRaisesExceptionIfPositionIsBelowMin(self):
        Volume = Knob("Volume")
        self.assertRaises(ValueError, Volume._validate_provided_position, -2)
    
    def test_ValidatePositionRaisesExceptionIfPositionIsAboveMax(self):
        Volume = Knob("Volume")
        self.assertRaises(ValueError, Volume._validate_provided_position, 12)

    def test_TurnToWithValidValueSetsNewValue(self):
        Volume = Knob("Volume")
        for setting in range(int(Volume._max_value)+1):
            Volume.Turn_To(setting)
            self.assertEqual(Volume._current_position, setting)
            
    def test_TurnToWithValidTooLargeRaisesException(self):
        Volume = Knob("Volume")
        self.assertRaises(ValueError, Volume.Turn_To, 11)
        
    def test_TurnToWithValidTooSmallRaisesException(self):
        Volume = Knob("Volume")
        self.assertRaises(ValueError, Volume.Turn_To, -1)

    def test_GetCurrentPositionReturnsCorrectPosition(self):
        Volume = Knob("Volume")
        Volume.Turn_To(6.6)
        self.assertEqual(Volume.Current_Position(), 6.6)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()