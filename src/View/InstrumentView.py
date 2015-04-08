'''
Created on Apr 8, 2015

@author: desposito
'''
from Tkinter import Frame, Listbox

class InstrumentView(Frame):
    '''
    Provides a frame to select the instrument and instrument parameters for the signal chain.
    '''

    AVAILABLE_INSTRUMENTS = ['Gibson Les Paul',
                             'Gibson SG',
                             'Suzuki M',
                             'Ibanez BTB Bass']

    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.InstrumentsList = Listbox(self.parent, selectmode="single")
        
        for instrument in self.AVAILABLE_INSTRUMENTS:
            self.InstrumentsList.insert("end", instrument)
            
        self.InstrumentsList.pack()