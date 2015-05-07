'''
Created on Mar 16, 2015

@author: desposito
'''
import unittest

from model.pedals.compressor import Compressor


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        comp = Compressor()
        self.assertEqual(comp.get_current_active_state(), "Off")
        self.assertEqual(comp.level.current_position, 0.0)
        self.assertEqual(comp.tone.current_position, 0.0)
        self.assertEqual(comp.attack.current_position, 0.0)
        self.assertEqual(comp.sustain.current_position, 0.0)
        self.assertIsNone(comp.connected_device.device)
    
    def test_ConstructorWithCustomLevel(self):
        
        comp = Compressor(level=7.8)
        self.assertEqual(comp.level.current_position, 7.8)
    
    def test_ConstructorWithCustomTone(self):
        
        comp = Compressor(tone=3.4)
        self.assertEqual(comp.tone.current_position, 3.4)
        
    def test_ConstructorWithCustomAttack(self):
        
        comp = Compressor(attack=5.6)
        self.assertEqual(comp.attack.current_position, 5.6)

    def test_ConstructorWithCustomSustain(self):
        
        comp = Compressor(sustain=1.2)
        self.assertEqual(comp.sustain.current_position, 1.2)
    
    def test_ConstructWithLowLevelRaisesException(self):
        
        self.assertRaises(ValueError, Compressor, level=-1)
        
    def test_ConstructWithHighLevelRaisesException(self):
        
        self.assertRaises(ValueError, Compressor, level=11)
        
    def test_NonNumericLevelRaisesException(self):
        
        self.assertRaises(TypeError, Compressor, level="threve")
    
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

    def test_ConstructWithLowSustainRaisesException(self):
        
        self.assertRaises(ValueError, Compressor, sustain=-1)
        
    def test_ConstructWithHighSustainRaisesException(self):
        
        self.assertRaises(ValueError, Compressor, sustain=11)
    
    def test_NonNumericSustainRaisesException(self):
        
        self.assertRaises(TypeError, Compressor, sustain="two")
    
    def test_Turn_Off_Deactivates_Compressor(self):
        
        comp = Compressor()
        comp.turn_off()
        self.assertEqual(comp.is_active(), False)
        self.assertEqual(comp.get_current_active_state(), "Off")
        
    def test_Turn_On_Activates_Compressor(self):
        
        comp = Compressor()
        comp.turn_off()
        self.assertEqual(comp.is_active(), False)
        self.assertEqual(comp.get_current_active_state(), "Off")
        comp.turn_on()
        self.assertEqual(comp.is_active(), True)
        self.assertEqual(comp.get_current_active_state(), "On")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()
    
    