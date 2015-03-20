'''
Created on Mar 16, 2015

@author: desposito
'''
import unittest
from Pedals.Gate import Gate
from Pedals.Compressor import Compressor

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        G1 = Gate()
        self.assertEqual(G1.Get_Current_Active_State(), "Off")
        self.assertEqual(G1.Get_Current_Mode(), "Gate")
        self.assertEqual(G1.Threshold.Current_Position(), 0.0)
        self.assertEqual(G1.Decay.Current_Position(), 0.0)
        self.assertIsNone(G1.ConnectedDevice)
        
    def test_ConstructWithCustomThreshold(self):
        G1 = Gate(threshold=3.4)
        self.assertEqual(G1.Threshold.Current_Position(), 3.4)

    def test_ConstructWithCustomDecay(self):
        G1 = Gate(decay=5.6)
        self.assertEqual(G1.Decay.Current_Position(), 5.6)

    def test_ConstructorWithDevice(self):
        C1 = Compressor()
        G1 = Gate(connected_device=C1)
        self.assertIsInstance(G1.ConnectedDevice, Compressor)

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
        G1 = Gate()
        G1.Turn_Off()
        self.assertEqual(G1.Is_Active(), False)
        self.assertEqual(G1.Get_Current_Active_State(), "Off")
        
    def test_Turn_On_Activates_Gate(self):
        G1 = Gate()
        G1.Turn_Off()
        self.assertEqual(G1.Is_Active(), False)
        self.assertEqual(G1.Get_Current_Active_State(), "Off")
        G1.Turn_On()
        self.assertEqual(G1.Is_Active(), True)
        self.assertEqual(G1.Get_Current_Active_State(), "On")
    
    def test_Set_Mode_To_Mute(self):
        G1 = Gate()
        G1.Set_Mode_To_Mute()
        self.assertEqual(G1.Get_Current_Mode(), "Mute")
        
    def test_Set_Mode_To_Gate(self):
        G1 = Gate()
        G1.Set_Mode_To_Mute()
        self.assertEqual(G1.Get_Current_Mode(), "Mute")
        G1.Set_Mode_To_Gate()
        self.assertEqual(G1.Get_Current_Mode(), "Gate")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()