'''
Created on Mar 17, 2015

@author: desposito
'''

import unittest

from model.instruments.suzuki_m import SuzukiM


class Test(unittest.TestCase):
    

    def test_ValidateDefaultConstructor(self):
        
        guitar = SuzukiM()
        self.assertEqual(guitar.volume.current_position, 10.0)
        self.assertEqual(guitar.bridge_tone.current_position, 10.0)
        self.assertEqual(guitar.middle_tone.current_position, 10.0)
        self.assertEqual(guitar.neck_tone.current_position, 10.0)
        self.assertEqual(guitar.pickup.position, "Bridge")
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()
    
    