'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from model.Instruments.SuzukiM import SuzukiM

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        S1 = SuzukiM()
        self.assertEqual(S1.Volume.Current_Position(), 10.0)
        self.assertEqual(S1.BridgeTone.Current_Position(), 10.0)
        self.assertEqual(S1.MiddleTone.Current_Position(), 10.0)
        self.assertEqual(S1.NeckTone.Current_Position(), 10.0)
        self.assertEqual(S1.Pickup.Current_Position(), "Bridge")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()