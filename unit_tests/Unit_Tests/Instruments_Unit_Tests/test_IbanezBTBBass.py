'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from model.Instruments.IbanezBTBBass import IbanezBTBBass

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        B1 = IbanezBTBBass()
        self.assertEqual(B1.Volume.Current_Position(), 10.0)
        self.assertEqual(B1.Pickup.Current_Position(), 0.0)
        self.assertEqual(B1.Bass.Current_Position(), 0.0)
        self.assertEqual(B1.Mid.Current_Position(), 0.0)
        self.assertEqual(B1.Treble.Current_Position(), 0.0)

    def test_VerifyPushPullPickupKnob(self):
        B1 = IbanezBTBBass()
        B1.Pickup.Turn_To(-5)
        self.assertEqual(B1.Pickup.Current_Position(), -5)
        B1.Pickup.Turn_To(5)
        self.assertEqual(B1.Pickup.Current_Position(), 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()