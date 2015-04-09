'''
Created on Mar 18, 2015

@author: Dave
'''
import unittest
from model.Interfaces.Focusrite_Saffire_Pro40 import InputChannel

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        C1 = InputChannel()
        self.assertEqual(C1.Level.Current_Position(), 0.0)
        self.assertIsNone(C1.ConnectedDevice.Device)
        self.assertIsNone(C1.InstrumentSwitch)
        self.assertIsNone(C1.PadSwitch)
        
    def test_ConstructorWithLevel(self):
        C1 = InputChannel(level=3.4)
        self.assertEqual(C1.Level.Current_Position(), 3.4)
        
    def test_AssignSwitches(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.InstrumentSwitch.Current_State())
        self.assertFalse(C1.PadSwitch.Current_State())
    
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
        self.assertTrue(C1.InstrumentSwitch.Current_State())
        
    def test_TurnOffInstrumentWithSwitchSetsSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Instrument_Level_On()
        self.assertTrue(C1.InstrumentSwitch.Current_State())
        C1.Turn_Instrument_Level_Off()
        self.assertFalse(C1.InstrumentSwitch.Current_State())
       
    def test_IsInstrumentOnWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(AttributeError, C1.Is_Instrument_Switch_On)
    
    def test_IsInstrumentOnWithSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Instrument_Level_On()
        self.assertTrue(C1.Is_Instrument_Switch_On())
        
    def test_IsInstrumentOnWithSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.Is_Instrument_Switch_On())    
        
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
        self.assertTrue(C1.PadSwitch.Current_State())
        
    def test_TurnPadOffWithSwitchSetsSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Pad_On()
        self.assertTrue(C1.PadSwitch.Current_State())
        C1.Turn_Pad_Off()
        
    def test_IsPadOnWithNoSwitchRaisesException(self):
        C1 = InputChannel()
        self.assertRaises(AttributeError, C1.Is_Pad_Switch_On)
    
    def test_IsPadOnWithSwitchOn(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        C1.Turn_Pad_On()
        self.assertTrue(C1.Is_Pad_Switch_On())
        
    def test_IsPadOnWithSwitchOff(self):
        C1 = InputChannel()
        C1.Assign_Switches()
        self.assertFalse(C1.Is_Pad_Switch_On())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()