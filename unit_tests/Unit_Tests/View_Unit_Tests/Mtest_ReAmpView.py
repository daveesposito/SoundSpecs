'''
Created on Apr 10, 2015

@author: desposito
'''
import unittest
from View.ReAmpView import ReAmpView
from Tkinter import Tk

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        R1 = ReAmpView(root)
        R1.pack()
        root.mainloop()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()