'''
Created on Mar 27, 2015

@author: Dave
'''
import unittest
from model.Signal_Chain import SignalChain

class Test(unittest.TestCase):

    def testDefaultConstructor(self):
        S1 = SignalChain()
        self.assertIsNone(S1.Instrument)
        self.assertListEqual(S1.Pedals, list())
        self.assertIsNone(S1.DI)
        self.assertIsNone(S1.Reamp)
        self.assertIsNone(S1.Amp)
        self.assertIsNone(S1.Input)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructor']
    unittest.main()