'''
Created on Mar 18, 2015

@author: desposito
'''
import unittest
from Mics.SM57 import SM57

class Test(unittest.TestCase):

    def testValidateDefaultConstructor(self):
        M1 = SM57("SM57A")
        self.assertEqual(M1.Name, "SM57A")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()