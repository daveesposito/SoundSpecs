'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.Utilities.Controls import Switch


class Test(unittest.TestCase):


    def test_DefaultConstructorValidation(self):
        
        channel = Switch("channel")
        self.assertEqual(channel.name, "channel")
        self.assertEqual(channel._true_value, "On")
        self.assertEqual(channel._false_value, "Off")
        self.assertTrue(channel.state)

    def test_SettingTrueValueInConstructor(self):
        
        channel = Switch("channel", "Drive")
        self.assertEqual(channel._true_value, "Drive")

    def test_SettingFalseValueInConstructor(self):
        
        channel = Switch("channel", "Drive", "Clean")
        self.assertEqual(channel._false_value, "Clean")

    def test_SettingCurrentStateInConstructor(self):
        
        channel = Switch("channel", "Drive", "Clean", False)
        self.assertFalse(channel.state)
        
    def test_SetStateToTrue(self):
        
        channel = Switch("channel", state=False)
        self.assertFalse(channel.state)
        channel.turn_on()
        self.assertTrue(channel.state)
        
    def test_SetStateToFalse(self):
        
        channel = Switch("channel")
        self.assertTrue(channel.state)
        channel.turn_off()
        self.assertFalse(channel.state)

    def test_ToggleToOn(self):
        
        channel = Switch("channel", state=False)
        self.assertFalse(channel.state)
        channel.toggle()
        self.assertTrue(channel.state)
        
    def test_ToggleToOff(self):
        
        channel = Switch("channel")
        self.assertTrue(channel.state)
        channel.toggle()
        self.assertFalse(channel.state)
        
    def test_MultipleToggles(self):
        
        channel = Switch("channel")
        self.assertTrue(channel.state)
        channel.toggle()
        self.assertFalse(channel.state)
        channel.toggle()
        self.assertTrue(channel.state)
        channel.toggle()
        self.assertFalse(channel.state)
        channel.toggle()
        self.assertTrue(channel.state)
        channel.toggle()
        self.assertFalse(channel.state)
        channel.toggle()
        self.assertTrue(channel.state)
    
    def test_GetNameOfTrueState(self):
        
        channel = Switch("channel", "Drive", "Clean")
        self.assertEqual(channel.state_name(), "Drive")
        
    def test_GetNameOfFalseState(self):
        
        channel = Switch("channel", "Drive", "Clean", False)
        self.assertEqual(channel.state_name(), "Clean")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_DefaultConstructorValidation']
    unittest.main()
    
    