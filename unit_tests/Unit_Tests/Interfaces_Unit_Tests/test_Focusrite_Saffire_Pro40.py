'''
Created on Mar 18, 2015

@author: desposito
'''

import unittest

from model.interfaces.focusrite_saffire_pro40 import Focusrite_Saffire_Pro40,\
    InputChannel, OutputChannel
from model.utilities.controls import Switch


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        self.assertEqual(len(aud_int.a_ins), 8)
        self.assertEqual(len(aud_int.a_outs), 8)
        self.assertIsInstance(aud_int.a_ins[0], InputChannel)
        self.assertIsInstance(aud_int.a_outs[0], OutputChannel)
        self.assertFalse(aud_int.phantom[0].state)
        self.assertFalse(aud_int.phantom[1].state)
        self.assertEqual(aud_int.main_level.current_position, 0)
        self.assertEqual(aud_int.phones_levels[0].current_position, 0)
        self.assertEqual(aud_int.phones_levels[1].current_position, 0)
        
    def test_ConstructorWithMainLevel(self):
        
        aud_int = Focusrite_Saffire_Pro40(main_level=3)
        self.assertEqual(aud_int.main_level.current_position, 3)
        
    def test_ConstructorWithPhones1(self):
        
        aud_int = Focusrite_Saffire_Pro40(phones_level_1=4)
        self.assertEqual(aud_int.phones_levels[0].current_position, 4)
        
    def test_ConstructorWithPhones2(self):
        
        aud_int = Focusrite_Saffire_Pro40(phones_level_2=5)
        self.assertEqual(aud_int.phones_levels[1].current_position, 5)

    def test_ConstructedInterfaceHasSwitchesOnChannels1And2(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        self.assertIsInstance(aud_int.a_ins[0].inst_sw, Switch)
        self.assertIsInstance(aud_int.a_ins[0].pad_sw, Switch)
        self.assertIsInstance(aud_int.a_ins[1].inst_sw, Switch)
        self.assertIsInstance(aud_int.a_ins[1].pad_sw, Switch)
        self.assertIsNone(aud_int.a_ins[2].inst_sw)
        self.assertIsNone(aud_int.a_ins[2].pad_sw)
        self.assertIsNone(aud_int.a_ins[3].inst_sw)
        self.assertIsNone(aud_int.a_ins[3].pad_sw)
        self.assertIsNone(aud_int.a_ins[4].inst_sw)
        self.assertIsNone(aud_int.a_ins[4].pad_sw)
        self.assertIsNone(aud_int.a_ins[5].inst_sw)
        self.assertIsNone(aud_int.a_ins[5].pad_sw)
        self.assertIsNone(aud_int.a_ins[6].inst_sw)
        self.assertIsNone(aud_int.a_ins[6].pad_sw)
        self.assertIsNone(aud_int.a_ins[7].inst_sw)
        self.assertIsNone(aud_int.a_ins[7].pad_sw)

    def test_Bank1PhantomSwitchReturnedIfChannelIs1Thru4(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        for channel in range(4):
            switch = aud_int._get_switch_based_on_channel(channel+1)
            self.assertEqual(switch.name, "Bank 1 Phantom Power")
            
    def test_Bank1PhantomSwitchReturnedIfChannelIs5Thru8(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        for channel in range(4):
            switch = aud_int._get_switch_based_on_channel(channel+5)
            self.assertEqual(switch.name, "Bank 2 Phantom Power")
            
    def test_GetSwitchMethodRaisesExceptionOnInvalidInput(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        self.assertRaises(ValueError, aud_int._get_switch_based_on_channel, 0)
        
    def test_Channels1thru4ReportFalseWhenPhantomPowerOff(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.phantom[0].turn_off()
        for channel in range(4):
            self.assertFalse(aud_int.is_channel_using_phantom_power(channel+1))

    def test_Channels1thru4ReportTrueWhenPhantomPowerOn(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.phantom[0].turn_on()
        for channel in range(4):
            self.assertTrue(aud_int.is_channel_using_phantom_power(channel+1))

    def test_Channels5thru8ReportFalseWhenPhantomPowerOff(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.phantom[1].turn_off()
        for channel in range(4):
            self.assertFalse(aud_int.is_channel_using_phantom_power(channel+5))

    def test_Channels5thru8ReportTrueWhenPhantomPowerOn(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.phantom[1].turn_on()
        for channel in range(4):
            self.assertTrue(aud_int.is_channel_using_phantom_power(channel+5))
            
    def test_SetOutputLevel(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.a_outs[0].level.turn_to(5)
        self.assertEqual(aud_int.a_outs[0].level.current_position, 5)
        
    def test_SetInputLevel(self):
        
        aud_int = Focusrite_Saffire_Pro40()
        aud_int.a_ins[0].level.turn_to(5)
        self.assertEqual(aud_int.a_ins[0].level.current_position, 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()