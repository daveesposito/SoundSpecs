'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.amplifier.masterchannel import MasterChannel


class Test(unittest.TestCase):
    

    def testDefaultConstructorValidation(self):
        
        master = MasterChannel()
        self.assertEqual(master.volume.current_position, 0.0)
        self.assertEqual(master.reverb.current_position, 0.0)
        self.assertEqual(master.send_level.current_position, 0.0)

    def testConstructorWithVolumeSetting(self):
        
        master = MasterChannel(volume=4)
        self.assertEqual(master.volume.current_position, 4)

    def testConstructorWithReverbSetting(self):
        
        master = MasterChannel(reverb=5.1)
        self.assertEqual(master.reverb.current_position, 5.1)
    
    def testConstructorWithSendLevelSetting(self):
        
        master = MasterChannel(send_level=9.9)
        self.assertEqual(master.send_level.current_position, 9.9)
        
    def testConstructorWithAllSettings(self):
        
        master = MasterChannel(3, 7, 9)
        self.assertEqual(master.volume.current_position, 3.0)
        self.assertEqual(master.reverb.current_position, 7.0)
        self.assertEqual(master.send_level.current_position, 9.0)
    
    def testReadDefaultChannelSelection(self):
        
        master = MasterChannel()
        self.assertEqual(master.current_type(), "Clean") 
    
    def testSelectCrunch(self):
        
        master = MasterChannel()
        master.select_drive()
        self.assertEqual(master.current_type(), "Drive")  
    
    def testSelectClean(self):
        
        master = MasterChannel()
        master.select_drive()
        self.assertEqual(master.current_type(), "Drive")
        master.select_clean()
        self.assertEqual(master.current_type(), "Clean") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    