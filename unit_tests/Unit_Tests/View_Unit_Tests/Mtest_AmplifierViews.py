'''
Created on Apr 9, 2015

@author: desposito
'''
import unittest
from View.AmplifierView.CleanChannelView import CleanChannelView
from View.AmplifierView.DriveChannelView import DriveChannelView
from View.AmplifierView.MasterChannelView import MasterChannelView
from View.AmplifierView import AmpflierView
from Tkinter import Tk

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST_Clean_Channel(self):
        root = Tk()
        C1 = CleanChannelView(root)
        C1.pack()
        root.mainloop()

    def test_MANUAL_UI_TEST_Drive_Channel(self):
        root = Tk()
        D1 = DriveChannelView(root)
        D1.pack()
        root.mainloop()
        
    def test_MANUAL_UI_TEST_Master_Channel(self):
        root = Tk()
        M1 = MasterChannelView(root)
        M1.pack()
        root.mainloop()
        
    def test_MANUAL_UI_TEST_Amplifier(self):
        root = Tk()
        A1 = AmpflierView(root)
        A1.pack()
        root.mainloop()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST_Clean_Channel']
    unittest.main()