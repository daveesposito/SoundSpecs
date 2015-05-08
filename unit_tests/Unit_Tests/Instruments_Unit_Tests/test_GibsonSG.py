'''
Created on Mar 17, 2015

@author: desposito
'''

import unittest

from model.instruments.gibson_sg import GibsonSG


class Test(unittest.TestCase):


    def test_ValidateDefaultConstructor(self):
        
        guitar = GibsonSG()
        self.assertEqual(guitar.bridge_vol.current_position, 10.0)
        self.assertEqual(guitar.bridge_tone.current_position, 10.0)
        self.assertEqual(guitar.neck_vol.current_position, 10.0)
        self.assertEqual(guitar.neck_tone.current_position, 10.0)
        self.assertEqual(guitar.pickup.position, "Bridge")
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()
    
    