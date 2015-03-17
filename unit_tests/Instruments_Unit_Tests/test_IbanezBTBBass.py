'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from Instruments.IbanezBTBBass import IbanazBTBBass

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        B1 = IbanazBTBBass()
        self.assertEqual(B1.Volume.Current_Position(), 10.0, "Volume not correctly initialized.")
        self.assertEqual(B1.Pickup.Current_Position(), 0.0, "Pickup not correctly initialized.")
        self.assertEqual(B1.Bass.Current_Position(), 0.0, "Bass not correctly initialized.")
        self.assertEqual(B1.Mid.Current_Position(), 0.0, "Mid not correctly initialized.")
        self.assertEqual(B1.Treble.Current_Position(), 0.0, "Treble not correctly initialized.")

    def test_VerifyPushPullPickupKnob(self):
        B1 = IbanazBTBBass()
        B1.Pickup.Turn_To(-5)
        self.assertEqual(B1.Pickup.Current_Position(), -5, "Failed to set Pickup.")
        B1.Pickup.Turn_To(5)
        self.assertEqual(B1.Pickup.Current_Position(), 5, "Failed to set Pickup.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()