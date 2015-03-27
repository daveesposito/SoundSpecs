'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from model.Utilities.Controls import Switch

class Test(unittest.TestCase):

    def test_DefaultConstructorValidation(self):
        Channel = Switch("Channel")
        self.assertEqual(Channel.Name, "Channel")
        self.assertEqual(Channel._true_value, "On")
        self.assertEqual(Channel._false_value, "Off")
        self.assertTrue(Channel._current_state)

    def test_SettingTrueValueInConstructor(self):
        Channel = Switch("Channel", "Drive")
        self.assertEqual(Channel._true_value, "Drive")

    def test_SettingFalseValueInConstructor(self):
        Channel = Switch("Channel", "Drive", "Clean")
        self.assertEqual(Channel._false_value, "Clean")

    def test_SettingCurrentStateInConstructor(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertFalse(Channel._current_state)
    
    def test_CurrentStateReturnsCorrectFalseState(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertFalse(Channel.Current_State())
        
    def test_CurrentStateReturnsCorrectTrueState(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State())
        
    def test_SetStateToTrue(self):
        Channel = Switch("Channel", current_state=False)
        self.assertFalse(Channel.Current_State())
        Channel.Turn_On()
        self.assertTrue(Channel.Current_State())
        
    def test_SetStateToFalse(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State())
        Channel.Turn_Off()
        self.assertFalse(Channel.Current_State())

    def test_ToggleToOn(self):
        Channel = Switch("Channel", current_state=False)
        self.assertFalse(Channel.Current_State())
        Channel.Toggle()
        self.assertTrue(Channel.Current_State())
        
    def test_ToggleToOff(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State())
        Channel.Toggle()
        self.assertFalse(Channel.Current_State())
        
    def test_MultipleToggles(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State())
        Channel.Toggle()
        self.assertFalse(Channel.Current_State())
        Channel.Toggle()
        self.assertTrue(Channel.Current_State())
        Channel.Toggle()
        self.assertFalse(Channel.Current_State())
        Channel.Toggle()
        self.assertTrue(Channel.Current_State())
        Channel.Toggle()
        self.assertFalse(Channel.Current_State())
        Channel.Toggle()
        self.assertTrue(Channel.Current_State())
    
    def test_GetNameOfTrueState(self):
        Channel = Switch("Channel", "Drive", "Clean")
        self.assertEqual(Channel.Current_State_Name(), "Drive")
        
    def test_GetNameOfFalseState(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertEqual(Channel.Current_State_Name(), "Clean")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_DefaultConstructorValidation']
    unittest.main()