'''
Created on Mar 13, 2015

@author: desposito
'''
import unittest
from Utilities.Controls import Switch

class Test(unittest.TestCase):

    def test_DefaultConstructorValidation(self):
        Channel = Switch("Channel")
        self.assertEqual(Channel.Name, "Channel", "Name not correctly initialized.")
        self.assertEqual(Channel._true_value, "On", "True Value not correctly initialized.")
        self.assertEqual(Channel._false_value, "Off", "False Value not correctly initialzied.")
        self.assertTrue(Channel._current_state, "Current state not correctly initialized.")

    def test_SettingTrueValueInConstructor(self):
        Channel = Switch("Channel", "Drive")
        self.assertEqual(Channel._true_value, "Drive", "True Value not correctly initialized.")

    def test_SettingFalseValueInConstructor(self):
        Channel = Switch("Channel", "Drive", "Clean")
        self.assertEqual(Channel._false_value, "Clean", "False Value not correctly initialized.")

    def test_SettingCurrentStateInConstructor(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertFalse(Channel._current_state, "Current state not correctly initialized.")
    
    def test_CurrentStateReturnsCorrectFalseState(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertFalse(Channel.Current_State(), "Current state not correctly read.")
        
    def test_CurrentStateReturnsCorrectTrueState(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State(), "Current state not correctly read.")
        
    def test_SetStateToTrue(self):
        Channel = Switch("Channel", current_state=False)
        self.assertFalse(Channel.Current_State(), "Failed to correctly initialize.")
        Channel.Turn_On()
        self.assertTrue(Channel.Current_State(), "Failed to set switch on.")
        
    def test_SetStateToFalse(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State(), "Failed to correctly initialize.")
        Channel.Turn_Off()
        self.assertFalse(Channel.Current_State(), "Failed to set switch off.")

    def test_ToggleToOn(self):
        Channel = Switch("Channel", current_state=False)
        self.assertFalse(Channel.Current_State(), "Failed to correctly initialize.")
        Channel.Toggle()
        self.assertTrue(Channel.Current_State(), "Failed to set switch on.")
        
    def test_ToggleToOff(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State(), "Failed to correctly initialize.")
        Channel.Toggle()
        self.assertFalse(Channel.Current_State(), "Failed to set switch off.")
        
    def test_MultipleToggles(self):
        Channel = Switch("Channel")
        self.assertTrue(Channel.Current_State(), "Failed to correctly initialize.")
        Channel.Toggle()
        self.assertFalse(Channel.Current_State(), "Failed to set switch off.")
        Channel.Toggle()
        self.assertTrue(Channel.Current_State(), "Failed to set switch on.")
        Channel.Toggle()
        self.assertFalse(Channel.Current_State(), "Failed to set switch off.")
        Channel.Toggle()
        self.assertTrue(Channel.Current_State(), "Failed to set switch on.")
        Channel.Toggle()
        self.assertFalse(Channel.Current_State(), "Failed to set switch off.")
        Channel.Toggle()
        self.assertTrue(Channel.Current_State(), "Failed to set switch on.")
    
    def test_GetNameOfTrueState(self):
        Channel = Switch("Channel", "Drive", "Clean")
        self.assertEqual(Channel.Current_State_Name(), "Drive", "Failed to get correct state name.")
        
    def test_GetNameOfFalseState(self):
        Channel = Switch("Channel", "Drive", "Clean", False)
        self.assertEqual(Channel.Current_State_Name(), "Clean", "Failed to get correct state name.")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_DefaultConstructorValidation']
    unittest.main()