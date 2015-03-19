'''
Created on Mar 18, 2015

@author: Dave
'''
import unittest
from Interfaces.Focusrite_Saffire_Pro40 import InputChannel
from Mics.SM57 import SM57

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        C1 = InputChannel()
        self.assertEqual(C1.Level.Current_Position(), 0.0, "Level not initialized.")
        self.assertIsNone(C1.ConnectedDevice, "Connected device was added some how.")
        self.assertIsNone(C1.InstrumentSwitch, "Instrument switch not none.")
        self.assertIsNone(C1.PadSwitch, "Pad switch not none.")
        
    def test_ConstructorWithLevel(self):
        C1 = InputChannel(level=3.4)
        self.assertEqual(C1.Level.Current_Position(), 3.4, "Level not set.")
        
    def test_ConstructorWithDevice(self):
        M1 = SM57("SM57A")
        C1 = InputChannel(connected_device=M1)
        self.assertIsInstance(C1.ConnectedDevice, SM57, "Didn't set device to SM57 object.")
        
    def test_AssignSwitches(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.InstrumentSwitch.Current_State(), "Didn't set switch object.")
        self.assertFalse(C1.PadSwitch.Current_State(), "Didn't set switch object.")
    
    def test_TurnOnInstrumentWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(TypeError, C1.Turn_Instrument_Level_On)
    
    def test_TurnOffInstrumentWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(TypeError, C1.Turn_Instrument_Level_Off)
            
    def test_TurnOnInstrumentWithSwitchSetsSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Instrument_Level_On()
        self.assertTrue(C1.InstrumentSwitch.Current_State(), "Didn't turn on switch.")
        
    def test_TurnOffInstrumentWithSwitchSetsSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Instrument_Level_On()
        self.assertTrue(C1.InstrumentSwitch.Current_State(), "Didn't turn on switch.")
        C1.Turn_Instrument_Level_Off()
        self.assertFalse(C1.InstrumentSwitch.Current_State(), "Didn't turn off switch.")
       
    def test_IsInstrumentOnWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(AttributeError, C1.Is_Instrument_Switch_On)
    
    def test_IsInstrumentOnWithSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Instrument_Level_On()
        self.assertTrue(C1.Is_Instrument_Switch_On(), "Switch not on.")
        
    def test_IsInstrumentOnWithSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.Is_Instrument_Switch_On(), "Switch not off.")    
        
    def test_TurnOnPadWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(TypeError, C1.Turn_Pad_On)
        
    def test_TurnOffPadWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(TypeError, C1.Turn_Pad_Off)
        
    def test_TurnPadOnWithSwitchSetsSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Pad_On()
        self.assertTrue(C1.PadSwitch.Current_State(), "Switch not on.")
        
    def test_TurnPadOffWithSwitchSetsSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Pad_On()
        self.assertTrue(C1.PadSwitch.Current_State(), "Switch not on.")
        C1.Turn_Pad_Off()
        
    def test_IsPadOnWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(AttributeError, C1.Is_Pad_Switch_On)
    
    def test_IsPadOnWithSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Pad_On()
        self.assertTrue(C1.Is_Pad_Switch_On(), "Switch not on.")
        
    def test_IsPadOnWithSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.Is_Pad_Switch_On(), "Switch not off.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()