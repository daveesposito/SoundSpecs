'''
Created on Apr 9, 2015

@author: desposito
'''
import unittest
from View.PedalsView import PedalsView
from Tkinter import Tk

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        PView = PedalsView(root)
        PView.pack()
        root.mainloop()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()