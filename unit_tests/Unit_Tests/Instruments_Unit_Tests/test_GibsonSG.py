'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from model.Instruments.GibsonSG import GibsonSG

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        G1 = GibsonSG()
        self.assertEqual(G1.BridgeVolume.Current_Position(), 10.0)
        self.assertEqual(G1.BridgeTone.Current_Position(), 10.0)
        self.assertEqual(G1.NeckVolume.Current_Position(), 10.0)
        self.assertEqual(G1.NeckTone.Current_Position(), 10.0)
        self.assertEqual(G1.Pickup.Current_Position(), "Bridge")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()