'''
Created on Mar 16, 2015

@author: desposito
'''
import unittest
from model.pedals.gate import Gate, Send
from model.pedals.compressor import Compressor


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        gate = Gate()
        self.assertEqual(gate.get_current_active_state(), "Off")
        self.assertEqual(gate.get_current_mode(), "Gate")
        self.assertEqual(gate.threshold.current_position, 0.0)
        self.assertEqual(gate.decay.current_position, 0.0)
        self.assertIsNone(gate.connected_device.device)
        self.assertIsNone(gate.return_.device)
        
    def test_ConstructWithCustomThreshold(self):
        gate = Gate(threshold=3.4)
        self.assertEqual(gate.threshold.current_position, 3.4)

    def test_ConstructWithCustomDecay(self):
        gate = Gate(decay=5.6)
        self.assertEqual(gate.decay.current_position, 5.6)

    def test_ConstructWithLowThresholdRaisesException(self):
        self.assertRaises(ValueError, Gate, threshold=-1)
        
    def test_ConstructWithHighThresholdRaisesException(self):
        self.assertRaises(ValueError, Gate, threshold=11)
    
    def test_NonNumericThresholdRaisesException(self):
        self.assertRaises(TypeError, Gate, threshold="two")
        
    def test_ConstructWithLowDecayRaisesException(self):
        self.assertRaises(ValueError, Gate, decay=-1)
        
    def test_ConstructWithHighDecayRaisesException(self):
        self.assertRaises(ValueError, Gate, decay=11)
        
    def test_NonNumericDecayRaisesException(self):
        self.assertRaises(TypeError, Gate, decay="threve")
        
    def test_Turn_Off_Deactivates_Gate(self):
        gate = Gate()
        gate.turn_off()
        self.assertEqual(gate.is_active(), False)
        self.assertEqual(gate.get_current_active_state(), "Off")
        
    def test_Turn_On_Activates_Gate(self):
        gate = Gate()
        gate.turn_off()
        self.assertEqual(gate.is_active(), False)
        self.assertEqual(gate.get_current_active_state(), "Off")
        gate.turn_on()
        self.assertEqual(gate.is_active(), True)
        self.assertEqual(gate.get_current_active_state(), "On")
    
    def test_Set_Mode_To_Mute(self):
        gate = Gate()
        gate.set_mode_to_mute()
        self.assertEqual(gate.get_current_mode(), "Mute")
        
    def test_Set_Mode_To_Gate(self):
        gate = Gate()
        gate.set_mode_to_mute()
        self.assertEqual(gate.get_current_mode(), "Mute")
        gate.set_mode_to_gate()
        self.assertEqual(gate.get_current_mode(), "Gate")
        
    def test_AssignOtherInputToSend(self):
        
        comp = Compressor()
        gate = Gate()
        comp.connected_device = gate.send
        self.assertIsInstance(comp.connected_device, Send)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()