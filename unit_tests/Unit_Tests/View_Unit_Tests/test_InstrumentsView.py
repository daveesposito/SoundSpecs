'''
Created on Apr 8, 2015

@author: desposito
'''
import unittest
from Tkinter import Tk
from View.InstrumentView import InstrumentView

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        IView = InstrumentView(root)
        IView.pack()
        root.mainloop()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()