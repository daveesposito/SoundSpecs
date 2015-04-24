'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame, Label, Entry, Button
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
        self._interfacesleft = Frame(self.parent)
        self._interfacesright = Frame(self.parent)
        
        self.Instrument = InstrumentView(self._left)
        self.Pedals1 = PedalsView(self._left)
        self.Pedals2 = PedalsView(self._left)
        self.DI = DIView(self._middle)
        self.ReAmp = ReAmpView(self._middle)
        self.Amp = AmpflierView(self._middle)
        self._ampinputframe = Frame(self._middle)
        self._ampinputlabel = Label(self._ampinputframe, text="Amp Input", anchor="w")
        self.AmpInput = Entry(self._ampinputframe, exportselection=False)
        self.Mics1 = MicView(self._right)
        self.Mics2 = MicView(self._right)
        self.Mics3 = MicView(self._right)
        
        self.SaveButton = Button(self._left, text = "Save", width = 15)
        self.LoadButton = Button(self._left, text = "Load", width = 15)
        
        self.Channel1 = Focusrite_InputView(self._interfacesleft)
        self.Channel2 = Focusrite_InputView(self._interfacesleft)
        self.Channel3 = Focusrite_InputView(self._interfacesleft)
        self.Channel4 = Focusrite_InputView(self._interfacesleft)
        
        self.Channel5 = Focusrite_InputView(self._interfacesright)
        self.Channel6 = Focusrite_InputView(self._interfacesright)
        self.Channel7 = Focusrite_InputView(self._interfacesright)
        self.Channel8 = Focusrite_InputView(self._interfacesright)
        
        self._left.pack(side="left", anchor="n")
        self._middle.pack(side="left", anchor="n")
        self._right.pack(side="left", anchor="n")
        self._interfacesleft.pack(side="left", anchor="n")
        self._interfacesright.pack(side="left", anchor="n")
        
        self.SaveButton.pack(pady = 30)
        self.LoadButton.pack(pady = 15)
        
        self.DI.pack()
        self.ReAmp.pack()        
        self.Amp.pack()
        self._ampinputframe.pack()
        self._ampinputlabel.pack(side="left")
        self.AmpInput.pack(side="left")
        
        self.Channel1.pack()
        self.Channel2.pack()
        self.Channel3.pack()
        self.Channel4.pack()
        self.Channel5.pack()
        self.Channel6.pack()
        self.Channel7.pack()
        self.Channel8.pack()