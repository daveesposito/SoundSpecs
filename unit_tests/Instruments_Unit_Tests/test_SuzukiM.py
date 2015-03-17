'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from Instruments.SuzukiM import SuzukiM

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        S1 = SuzukiM()
        self.assertEqual(S1.Volume.Current_Position(), 10.0, "Volume not correctly initialized.")
        self.assertEqual(S1.BridgeTone.Current_Position(), 10.0, "Bridge Tone not correctly initialized.")
        self.assertEqual(S1.MiddleTone.Current_Position(), 10.0, "Middle Tone not correctly initialized.")
        self.assertEqual(S1.NeckTone.Current_Position(), 10.0, "Neck Tone not correctly initialized.")
        self.assertEqual(S1.Pickup.Current_Position(), "Bridge", "Pickup not correctly initialized.")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()