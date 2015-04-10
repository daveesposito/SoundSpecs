'''
Created on Apr 10, 2015

@author: desposito
'''
import unittest
from View.MicView import MicView
from Tkinter import Tk

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        M1 = MicView(root)
        M1.pack()
        root.mainloop()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()