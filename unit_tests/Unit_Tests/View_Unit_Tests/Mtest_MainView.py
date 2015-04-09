'''
Created on Apr 9, 2015

@author: desposito
'''
import unittest
from Tkinter import Tk
from View import MainView

class Test(unittest.TestCase):


    def test_MANUAL_UI_TEST(self):
        root = Tk()
        app = MainView(root)
        app.pack(expand=True, fill="both")
        root.update_idletasks()
        root.mainloop()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_MANUAL_UI_TEST']
    unittest.main()