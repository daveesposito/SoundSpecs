'''
Created on Mar 18, 2015

@author: desposito
'''

import unittest

from model.mics.sm57 import SM57


class Test(unittest.TestCase):


    def testValidateDefaultConstructor(self):
        
        mic = SM57("SM57A")
        self.assertEqual(mic.name, "SM57A")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()
    
    