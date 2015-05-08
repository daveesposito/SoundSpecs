'''
Created on Mar 17, 2015

@author: desposito
'''

import unittest

from model.instruments.ibanez_btb_bass import IbanezBTBBass


class Test(unittest.TestCase):
    

    def test_ValidateDefaultConstructor(self):
        
        bass = IbanezBTBBass()
        self.assertEqual(bass.volume.current_position, 10.0)
        self.assertEqual(bass.pickup.current_position, 0.0)
        self.assertEqual(bass.bass.current_position, 0.0)
        self.assertEqual(bass.mid.current_position, 0.0)
        self.assertEqual(bass.treble.current_position, 0.0)

    def test_VerifyPushPullPickupKnob(self):
        
        bass = IbanezBTBBass()
        bass.pickup.turn_to(-5)
        self.assertEqual(bass.pickup.current_position, -5)
        bass.pickup.turn_to(5)
        self.assertEqual(bass.pickup.current_position, 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()