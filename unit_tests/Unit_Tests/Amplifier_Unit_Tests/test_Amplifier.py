'''
Created on Mar 19, 2015

@author: desposito
'''
import unittest
from Amplifier import Amplifier
from Amplifier.CleanChannel import CleanChannel
from Amplifier.DriveChannel import DriveChannel
from Amplifier.MasterChannel import MasterChannel

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        A1 = Amplifier()
        self.assertIsNone(A1.ConnectedDevices, "Device connected.")
        self.assertIsInstance(A1.Clean, CleanChannel, "CleanChannel not assigned.")
        self.assertIsInstance(A1.Drive, DriveChannel, "DriveChannel not assigned.")
        self.assertIsInstance(A1.Master, MasterChannel, "MasterChannel not assigned.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()