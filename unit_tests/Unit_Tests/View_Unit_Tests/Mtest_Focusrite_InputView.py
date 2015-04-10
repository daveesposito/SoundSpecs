'''
Created on Apr 10, 2015

@author: desposito
'''
import unittest
from View.Focusrite_InputView import Focusrite_InputView
from Tkinter import Tk

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        F1 = Focusrite_InputView(root)
        F1.pack()
        root.mainloop()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()