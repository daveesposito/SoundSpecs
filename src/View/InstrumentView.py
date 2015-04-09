'''
Created on Apr 8, 2015

@author: desposito
'''
from Tkinter import Frame, Listbox, LabelFrame, Spinbox, Label
from model.Instruments.GibsonLesPaul import GibsonLesPaul
from model.Instruments.GibsonSG import GibsonSG
from model.Instruments.IbanezBTBBass import IbanezBTBBass
from model.Instruments.SuzukiM import SuzukiM
from model.Utilities.Controls import Multiselect

class InstrumentView(Frame):
    '''
    Provides a frame to select the instrument and instrument parameters for the signal chain.
    '''

    AVAILABLE_INSTRUMENTS = {'Gibson Les Paul':GibsonLesPaul(),
                             'Gibson SG':GibsonSG(),
                             'Suzuki M':SuzukiM(),
                             'Ibanez BTB Bass':IbanezBTBBass(),
                             '<none>':""}

    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._labelframe = LabelFrame(self.parent, text="Select Instrument")
        self.InstrumentsList = Listbox(self._labelframe, selectmode="single", height=len(self.AVAILABLE_INSTRUMENTS))
        self._controlsframe = Frame(self._labelframe, width=173, height=125)
        self.Controls = list()
        self.ControlItems = dict()
        self.ControlLabels = dict()
        
        for instrument in self.AVAILABLE_INSTRUMENTS.keys():
            self.InstrumentsList.insert("end", instrument)
            
        self.InstrumentsList.bind('<<ListboxSelect>>', self.loadControls)
            
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.rowconfigure(0, weight=1)
        self._labelframe.pack(expand=True, fill="both")
        self.InstrumentsList.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._controlsframe.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
    def loadControls(self, evt):
        selectedInstrument = self.InstrumentsList.selection_get()
        if selectedInstrument != ():
            if selectedInstrument == '<none>':
                self._clearInstruments()
            else:
                self._clearInstruments()
                self._listControlsForSelectedInstrument(selectedInstrument)
                self._createControlsForSelectedInstrument()
                self._placeControls()
    
    def _clearInstruments(self):
        for control in self.ControlItems.values():
            control.grid_forget()
        for label in self.ControlLabels.values():
            label.grid_forget()
        self.Controls = list()
        self.ControlItems = dict()
        self.ControlLabels = dict()
        self.master.update_idletasks()
    
    def _listControlsForSelectedInstrument(self, selectedInstrument):
        selectedInstrumentObject = self.AVAILABLE_INSTRUMENTS[selectedInstrument]
        controls = selectedInstrumentObject.__dict__
        for item in controls.keys():
            self.Controls.append(controls[item])
                
    def _createControlsForSelectedInstrument(self):
        for control in self.Controls:
            if isinstance(control, Multiselect):
                self.ControlItems[control.Name] = self._loadMultiselectControl(control)
            else:
                self.ControlItems[control.Name] = self._loadKnobControl(control)
            self.ControlLabels[control.Name] = Label(self._controlsframe, text=control.Name, anchor="w", width=12)
    
    def _placeControls(self):
        row = 0
        for control in self.Controls:
            self.ControlLabels[control.Name].grid(column=0, row=row, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            self.ControlItems[control.Name].grid(column=1, row=row, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            row = row + 1
            
    def _loadKnobControl(self, modelcontrol):
        return Spinbox(self._controlsframe, from_=modelcontrol._min_value, to_=modelcontrol._max_value, width=10)
    
    def _loadMultiselectControl(self, modelcontrol):
        vals = ()
        for pos in modelcontrol.selections:
            vals = vals + (pos,)
        return Spinbox(self._controlsframe, values=vals, width=10)
        
            