'''
Created on Mar 18, 2015

@author: desposito
'''
import unittest
from Interfaces.Focusrite_Saffire_Pro40 import Focusrite_Saffire_Pro40

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        F1 = Focusrite_Saffire_Pro40()
        self.assertEqual(len(F1.AnalogInputs), 8, "Analog Inputs not intiialized.")
        self.assertEqual(F1.AnalogInputs[0].Level.Current_Position(), 0, "Level not set")
        self.assertFalse(F1.PhantomPower[0].Current_State(), "Phantom power not off.")
        self.assertFalse(F1.PhantomPower[1].Current_State(), "Phantom power not off.")

    def test_ConstructedInterfaceHasSwitchesOnChannels1And2(self):
        F1 = Focusrite_Saffire_Pro40()
        self.assertFalse(F1.AnalogInputs[0].Is_Instrument_Switch_On(), "Switch not off.")
        self.assertFalse(F1.AnalogInputs[1].Is_Instrument_Switch_On(), "Switch not off.")
        self.assertRaises(AttributeError, F1.AnalogInputs[2].Is_Instrument_Switch_On)
        self.assertRaises(AttributeError, F1.AnalogInputs[3].Is_Instrument_Switch_On)
        self.assertRaises(AttributeError, F1.AnalogInputs[4].Is_Instrument_Switch_On)
        self.assertRaises(AttributeError, F1.AnalogInputs[5].Is_Instrument_Switch_On)
        self.assertRaises(AttributeError, F1.AnalogInputs[6].Is_Instrument_Switch_On)
        self.assertRaises(AttributeError, F1.AnalogInputs[7].Is_Instrument_Switch_On)

    def test_Bank1PhantomSwitchReturnedIfChannelIs1Thru4(self):
        F1 = Focusrite_Saffire_Pro40()
        for channel in range(4):
            switch = F1._Get_Switch_Based_On_Channel(channel + 1)
            self.assertEqual(switch.Name, "Bank 1 Phantom Power", "Didn't get right switch.")
            
    def test_Bank1PhantomSwitchReturnedIfChannelIs5Thru8(self):
        F1 = Focusrite_Saffire_Pro40()
        for channel in range(4):
            switch = F1._Get_Switch_Based_On_Channel(channel + 5)
            self.assertEqual(switch.Name, "Bank 2 Phantom Power", "Didn't get right switch.")
            
    def test_GetSwitchMethodRaisesExceptionOnInvalidInput(self):
        F1 = Focusrite_Saffire_Pro40()
        self.assertRaises(ValueError, F1._Get_Switch_Based_On_Channel, 0)
        
    def test_Channels1thru4ReportFalseWhenPhantomPowerOff(self):
        F1 = Focusrite_Saffire_Pro40()
        F1.PhantomPower[1].Turn_On()
        for channel in range(4):
            self.assertFalse(F1.IsChannelUsingPhantomPower(channel + 1), "Phantom power not off.")

    def test_Channels1thru4ReportTrueWhenPhantomPowerOn(self):
        F1 = Focusrite_Saffire_Pro40()
        F1.PhantomPower[0].Turn_On()
        for channel in range(4):
            self.assertTrue(F1.IsChannelUsingPhantomPower(channel + 1), "Phantom power not on.")

    def test_Channels5thru8ReportFalseWhenPhantomPowerOff(self):
        F1 = Focusrite_Saffire_Pro40()
        F1.PhantomPower[0].Turn_On()
        for channel in range(4):
            self.assertFalse(F1.IsChannelUsingPhantomPower(channel + 5), "Phantom power not off.")

    def test_Channels5thru8ReportTrueWhenPhantomPowerOn(self):
        F1 = Focusrite_Saffire_Pro40()
        F1.PhantomPower[1].Turn_On()
        for channel in range(4):
            self.assertTrue(F1.IsChannelUsingPhantomPower(channel + 5), "Phantom power not on.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()