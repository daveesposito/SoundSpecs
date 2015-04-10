'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame, Label, Entry
from View.AmplifierView import AmpflierView
from View.InstrumentView import InstrumentView
from View.PedalsView import PedalsView
from View.MicView import MicView
from View.DIView import DIView
from View.ReAmpView import ReAmpView
from View.Focusrite_InputView import Focusrite_InputView

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
        self._interfaces = Frame(self.parent)
        
        self.Instrument = InstrumentView(self._left)
        self.Pedals1 = PedalsView(self._left)
        self.Pedals2 = PedalsView(self._left)
        self.Amp = AmpflierView(self._middle)
        self._ampinputframe = Frame(self._middle)
        self._ampinputlabel = Label(self._ampinputframe, text="Amp Input", anchor="w")
        self.AmpInput = Entry(self._ampinputframe, exportselection=False)
        self.Mics1 = MicView(self._right)
        self.Mics2 = MicView(self._right)
        self.Mics3 = MicView(self._right)
        self.DI = DIView(self._interfaces)
        self.ReAmp = ReAmpView(self._interfaces)
        self.Interface = Focusrite_InputView(self._interfaces)
        
        self._left.pack(side="left")
        self._middle.pack(side="left")
        self._right.pack(side="left")
        self._interfaces.pack(side="left")
                
        self.Amp.pack()
        self._ampinputframe.pack()
        self._ampinputlabel.pack(side="left")
        self.AmpInput.pack(side="left")
        
        self.DI.pack()
        self.ReAmp.pack()
        self.Interface.pack()