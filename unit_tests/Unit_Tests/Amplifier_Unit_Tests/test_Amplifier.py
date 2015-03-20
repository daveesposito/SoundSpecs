'''
Created on Mar 19, 2015

@author: desposito
'''
import unittest
from Amplifier import Amplifier
from Amplifier.CleanChannel import CleanChannel
from Amplifier.DriveChannel import DriveChannel
from Amplifier.MasterChannel import MasterChannel
from Pedals.Compressor import Compressor

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        A1 = Amplifier()
        self.assertIsNone(A1.ConnectedDevices, "Device connected.")
        self.assertIsInstance(A1.Clean, CleanChannel, "CleanChannel not assigned.")
        self.assertIsInstance(A1.Drive, DriveChannel, "DriveChannel not assigned.")
        self.assertIsInstance(A1.Master, MasterChannel, "MasterChannel not assigned.")

    def test_ConstructorWithDevice(self):
        C1 = Compressor()
        A1 = Amplifier(C1)
        self.assertIsInstance(A1.ConnectedDevices, Compressor, "Compressor not connected.")

    def test_SetCleanNone(self):
        A1 = Amplifier()
        A1.Set_Clean_Channel()
        self.assertEqual(A1.Clean.Gain.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Bass.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Treble.Current_Position(), 0.0)
        
    def test_SetCleanGain(self):
        A1 = Amplifier()
        A1.Set_Clean_Channel(gain=4)
        self.assertEqual(A1.Clean.Gain.Current_Position(), 4.0)
        self.assertEqual(A1.Clean.Bass.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Treble.Current_Position(), 0.0)
        
    def test_SetCleanBass(self):
        A1 = Amplifier()
        A1.Set_Clean_Channel(bass = 8)
        self.assertEqual(A1.Clean.Gain.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Bass.Current_Position(), 8.0)
        self.assertEqual(A1.Clean.Treble.Current_Position(), 0.0)
        
    def test_SetCleanTreble(self):
        A1 = Amplifier()
        A1.Set_Clean_Channel(treble=9.9)
        self.assertEqual(A1.Clean.Gain.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Bass.Current_Position(), 0.0)
        self.assertEqual(A1.Clean.Treble.Current_Position(), 9.9)
        
    def test_SetCleanAll(self):
        A1 = Amplifier()
        A1.Set_Clean_Channel(1, 2, 3)
        self.assertEqual(A1.Clean.Gain.Current_Position(), 1)
        self.assertEqual(A1.Clean.Bass.Current_Position(), 2)
        self.assertEqual(A1.Clean.Treble.Current_Position(), 3)
        
    def test_SetDriveNone(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel()
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
    
    def test_SetDriveGain(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(gain=1)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 1)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
    
    def test_SetDriveBass(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(bass=2)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 2)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
    
    def test_SetDriveMid(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(mid=3)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 3)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
    
    def test_SetDriveTreble(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(treble=4)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 4)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
    
    def test_SetDriveContour(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(contour=5)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 5)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 0)
        
    def test_SetDriveVolume(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(volume=6)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 0)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 0)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 0)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 0)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 0)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 6)
        
    def test_SetDriveAll(self):
        A1 = Amplifier()
        A1.Set_Drive_Channel(6, 5, 4, 3, 2, 1)
        self.assertEqual(A1.Drive.Gain.Current_Position(), 6)
        self.assertEqual(A1.Drive.Bass.Current_Position(), 5)
        self.assertEqual(A1.Drive.Mid.Current_Position(), 4)
        self.assertEqual(A1.Drive.Treble.Current_Position(), 3)
        self.assertEqual(A1.Drive.Contour.Current_Position(), 2)
        self.assertEqual(A1.Drive.Volume.Current_Position(), 1)
    
    def test_SetMasterNone(self):
        A1= Amplifier()
        A1.Set_Master_Channel()
        self.assertEqual(A1.Master.Volume.Current_Position(), 0)
        self.assertEqual(A1.Master.Reverb.Current_Position(), 0)
        self.assertEqual(A1.Master.Send_Level.Current_Position(), 0)
        
    def test_SetMasterVolume(self):
        A1= Amplifier()
        A1.Set_Master_Channel(volume=4)
        self.assertEqual(A1.Master.Volume.Current_Position(), 4)
        self.assertEqual(A1.Master.Reverb.Current_Position(), 0)
        self.assertEqual(A1.Master.Send_Level.Current_Position(), 0)
        
    def test_SetMasterReverb(self):
        A1= Amplifier()
        A1.Set_Master_Channel(reverb=3)
        self.assertEqual(A1.Master.Volume.Current_Position(), 0)
        self.assertEqual(A1.Master.Reverb.Current_Position(), 3)
        self.assertEqual(A1.Master.Send_Level.Current_Position(), 0)
        
    def test_SetMasterSendLevel(self):
        A1= Amplifier()
        A1.Set_Master_Channel(send_level=2)
        self.assertEqual(A1.Master.Volume.Current_Position(), 0)
        self.assertEqual(A1.Master.Reverb.Current_Position(), 0)
        self.assertEqual(A1.Master.Send_Level.Current_Position(), 2)
    
    def test_SetMasterAll(self):
        A1= Amplifier()
        A1.Set_Master_Channel(1, 2, 3)
        self.assertEqual(A1.Master.Volume.Current_Position(), 1)
        self.assertEqual(A1.Master.Reverb.Current_Position(), 2)
        self.assertEqual(A1.Master.Send_Level.Current_Position(), 3)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ValidateDefaultConstructor']
    unittest.main()