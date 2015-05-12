'''
Created on Mar 18, 2015

@author: Dave
'''

import unittest

from model.interfaces.focusrite_saffire_pro40 import InputChannel


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        chan = InputChannel()
        self.assertEqual(chan.level.current_position, 0.0)
        self.assertIsNone(chan.connected_device.device)
        self.assertIsNone(chan.inst_sw)
        self.assertIsNone(chan.pad_sw)
        
    def test_ConstructorWithLevel(self):
        
        chan = InputChannel(level=3.4)
        self.assertEqual(chan.level.current_position, 3.4)
        
    def test_AssignSwitches(self):
        
        chan = InputChannel()
        chan._assign_switches()
        self.assertFalse(chan.inst_sw.state)
        self.assertFalse(chan.pad_sw.state)
    
    def test_TurnOnInstrumentWithNoSwitchRaisesException(self):
        
        chan = InputChannel()
        self.assertRaises(TypeError, chan.turn_instrument_level_on)
    
    def test_TurnOffInstrumentWithNoSwitchRaisesException(self):
        
        chan = InputChannel()
        self.assertRaises(TypeError, chan.turn_instrument_level_off)
            
    def test_TurnOnInstrumentWithSwitchSetsSwitchOn(self):
        
        chan = InputChannel()
        chan._assign_switches()
        chan.turn_instrument_level_on()
        self.assertTrue(chan.inst_sw.state)
        
    def test_TurnOffInstrumentWithSwitchSetsSwitchOff(self):
        
        chan = InputChannel()
        chan._assign_switches()
        chan.turn_instrument_level_on()
        self.assertTrue(chan.inst_sw.state)
        chan.turn_instrument_level_off()
        self.assertFalse(chan.inst_sw.state)    
        
    def test_TurnOnPadWithNoSwitchRaisesException(self):
        
        chan = InputChannel()
        self.assertRaises(TypeError, chan.turn_pad_on)
        
    def test_TurnOffPadWithNoSwitchRaisesException(self):
        
        chan = InputChannel()
        self.assertRaises(TypeError, chan.turn_pad_off)
        
    def test_TurnPadOnWithSwitchSetsSwitchOn(self):
        
        chan = InputChannel()
        chan._assign_switches()
        chan.turn_pad_on()
        self.assertTrue(chan.pad_sw.state)
        
    def test_TurnPadOffWithSwitchSetsSwitchOff(self):
        
        chan = InputChannel()
        chan._assign_switches()
        chan.turn_pad_on()
        self.assertTrue(chan.pad_sw.state)
        chan.turn_pad_off()
        self.assertFalse(chan.pad_sw.state)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()
    
    