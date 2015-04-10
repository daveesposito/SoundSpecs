'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame
from View.AmplifierView import AmpflierView
from View.InstrumentView import InstrumentView
from View.PedalsView import PedalsView
from View.MicView import MicView

class MainView(Frame):
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        self._left = Frame(self.parent)
        self._middle = Frame(self.parent)
        self._right = Frame(self.parent)
        
        self.Instrument = InstrumentView(self._left)
        self.Pedals1 = PedalsView(self._left)
        self.Pedals2 = PedalsView(self._left)
        self.Amp = AmpflierView(self._middle)
        self.Mics1 = MicView(self._right)
        self.Mics2 = MicView(self._right)
        
        self._left.pack(side="left")
        self._middle.pack(side="left")
        self._right.pack(side="left")
                
        
        
        self.Amp.pack()