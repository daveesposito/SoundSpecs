'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame
from View.AmplifierView import AmpflierView
from View.InstrumentView import InstrumentView
from View.PedalsView import PedalsView

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
        self._right = Frame(self.parent)
        
        self.Instrument = InstrumentView(self._left)
        self.Pedals1 = PedalsView(self._left)
        self.Pedals2 = PedalsView(self._left)
        self.Amp = AmpflierView(self._right)
        
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        
        #self.Instrument.grid(column=0, row=0)
        #self.Pedals1.grid(column=0, row=1)
        #self.Pedals2.grid(column=0, row=2)
        #self.Amp.grid(column=1, row=0, rowspan=3)
        
        self._left.pack(side="left")
        self._right.pack(side="right")
        
        self.Instrument.pack()
        self.Pedals1.pack()
        self.Pedals2.pack()
        
        self.Amp.pack()