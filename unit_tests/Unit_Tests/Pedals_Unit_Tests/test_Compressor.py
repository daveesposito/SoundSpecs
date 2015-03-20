'''
Created on Mar 16, 2015

@author: desposito
'''
import unittest
from Pedals.Compressor import Compressor
from Instruments.GibsonSG import GibsonSG

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        C1 = Compressor()
        self.assertEqual(C1.Get_Current_Active_State(), "Off")
        self.assertEqual(C1.Threshold.Current_Position(), 0.0)
        self.assertEqual(C1.Tone.Current_Position(), 0.0)
        self.assertEqual(C1.Attack.Current_Position(), 0.0)
        self.assertEqual(C1.Level.Current_Position(), 0.0)
        self.assertIsNone(C1.ConnectedDevice)

    def test_ConstructorWithCustomThreshold(self):
        C1 = Compressor(threshold=1.2)
        self.assertEqual(C1.Threshold.Current_Position(), 1.2)
        
    def test_ConstructorWithCustomTone(self):
        C1 = Compressor(tone=3.4)
        self.assertEqual(C1.Tone.Current_Position(), 3.4)
        
    def test_ConstructorWithCustomAttack(self):
        C1 = Compressor(attack=5.6)
        self.assertEqual(C1.Attack.Current_Position(), 5.6)
        
    def test_ConstructorWithCustomLevel(self):
        C1 = Compressor(level=7.8)
        self.assertEqual(C1.Level.Current_Position(), 7.8)

    def test_ConstructorWithDevice(self):
        G1 = GibsonSG()
        C1 = Compressor(connected_device=G1)
        self.assertIsInstance(C1.ConnectedDevice, GibsonSG)
    
    def test_ConstructWithLowThresholdRaisesException(self):
        self.assertRaises(ValueError, Compressor, threshold=-1)
        
    def test_ConstructWithHighThresholdRaisesException(self):
        self.assertRaises(ValueError, Compressor, threshold=11)
    
    def test_NonNumericThresholdRaisesException(self):
        self.assertRaises(TypeError, Compressor, threshold="two")
    
    def test_ConstructWithLowToneRaisesException(self):
        self.assertRaises(ValueError, Compressor, tone=-1)
        
    def test_ConstructWithHighToneRaisesException(self):
        self.assertRaises(ValueError, Compressor, tone=11)
        
    def test_NonNumericToneRaisesException(self):
        self.assertRaises(TypeError, Compressor, tone="threve")
        
    def test_ConstructWithLowAttackRaisesException(self):
        self.assertRaises(ValueError, Compressor, attack=-1)
        
    def test_ConstructWithHighAttackRaisesException(self):
        self.assertRaises(ValueError, Compressor, attack=11)
        
    def test_NonNumericAttackRaisesException(self):
        self.assertRaises(TypeError, Compressor, attack="threve")
        
    def test_ConstructWithLowLevelRaisesException(self):
        self.assertRaises(ValueError, Compressor, level=-1)
        
    def test_ConstructWithHighLevelRaisesException(self):
        self.assertRaises(ValueError, Compressor, level=11)
        
    def test_NonNumericLevelRaisesException(self):
        self.assertRaises(TypeError, Compressor, level="threve")

    def test_Turn_Off_Deactivates_Compressor(self):
        C1 = Compressor()
        C1.Turn_Off()
        self.assertEqual(C1.Is_Active(), False)
        self.assertEqual(C1.Get_Current_Active_State(), "Off")
        
    def test_Turn_On_Activates_Compressor(self):
        C1 = Compressor()
        C1.Turn_Off()
        self.assertEqual(C1.Is_Active(), False)
        self.assertEqual(C1.Get_Current_Active_State(), "Off")
        C1.Turn_On()
        self.assertEqual(C1.Is_Active(), True)
        self.assertEqual(C1.Get_Current_Active_State(), "On")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()