'''
Created on Mar 13, 2015

@author: desposito
'''

import unittest

from model.amplifier.masterchannel import MasterChannel


class Test(unittest.TestCase):
    

    def test_DefaultConstructorValidation(self):
        
        master = MasterChannel()
        self.assertEqual(master.volume.current_position, 0.0)
        self.assertEqual(master.reverb.current_position, 0.0)
        self.assertEqual(master.send_level.current_position, 0.0)

    def test_ConstructorWithVolumeSetting(self):
        
        master = MasterChannel(volume=4)
        self.assertEqual(master.volume.current_position, 4)

    def test_ConstructorWithReverbSetting(self):
        
        master = MasterChannel(reverb=5.1)
        self.assertEqual(master.reverb.current_position, 5.1)
    
    def test_ConstructorWithSendLevelSetting(self):
        
        master = MasterChannel(send_level=9.9)
        self.assertEqual(master.send_level.current_position, 9.9)
        
    def test_NonNumbericVolumeRaisesException(self):
        
        self.assertRaises(TypeError, MasterChannel, volume="volume")
        
    def test_NonNumbericReverbRaisesException(self):
        
        self.assertRaises(TypeError, MasterChannel, reverb="reverb")
        
    def test_NonNumbericSendLevelRaisesException(self):
        
        self.assertRaises(TypeError, MasterChannel, send_level="send")
        
    def test_ConstructorWithAllSettings(self):
        
        master = MasterChannel(3, 7, 9)
        self.assertEqual(master.volume.current_position, 3.0)
        self.assertEqual(master.reverb.current_position, 7.0)
        self.assertEqual(master.send_level.current_position, 9.0)
    
    def test_ReadDefaultChannelSelection(self):
        
        master = MasterChannel()
        self.assertEqual(master.current_type(), "Clean") 
    
    def test_SelectCrunch(self):
        
        master = MasterChannel()
        master.select_drive()
        self.assertEqual(master.current_type(), "Drive")  
    
    def test_SelectClean(self):
        
        master = MasterChannel()
        master.select_drive()
        self.assertEqual(master.current_type(), "Drive")
        master.select_clean()
        self.assertEqual(master.current_type(), "Clean") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultConstructorValidation']
    unittest.main()
    
    