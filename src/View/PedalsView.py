'''
Created on Apr 8, 2015

@author: desposito
'''
from Tkinter import Frame, Listbox, LabelFrame, Spinbox, Label, Radiobutton,\
    IntVar, Entry
from model.Pedals.Compressor import Compressor
from model.Pedals.Gate import Gate
from model.Utilities.Controls import Switch, Knob

class PedalsView(Frame):
    '''
    Provides a frame to select the Pedals and pedal parameters for the signal chain.
    '''

    AVAILABLE_PEDALS = {'Compressor':Compressor(),
                        'Gate':Gate(),
                        '<none>':""}

    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._labelframe = LabelFrame(self.parent, text="Select Pedal")
        self.PedalList = Listbox(self._labelframe, selectmode="single", height=len(self.AVAILABLE_PEDALS))
        self._controlsframe = Frame(self._labelframe, width=222, height=182)                                  
        self.Controls = list()
        self.ControlItems = dict()
        self.ControlLabels = dict()
        self.SwitchStates = dict()
        
        for pedal in self.AVAILABLE_PEDALS.keys():
            self.PedalList.insert("end", pedal)
            
        self.PedalList.bind('<<ListboxSelect>>', self.loadControls)
            
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.rowconfigure(0, weight=1)
        self._labelframe.pack(expand=True, fill="both")
        self.PedalList.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._controlsframe.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
    def loadControls(self, evt):
        selectedPedal = self.PedalList.selection_get()
        if selectedPedal != ():
            if selectedPedal == '<none>':
                self._clearPedals()
            else:
                self._clearPedals()
                self._listControlsForSelectedPedal(selectedPedal)
                self._createControlsForSelectedPedal()
                self._placeControls()
    
    def _clearPedals(self):
        for control in self.ControlItems.values():
            control.grid_forget()
        for label in self.ControlLabels.values():
            label.grid_forget()
        self.Controls = list()
        self.ControlItems = dict()
        self.ControlLabels = dict()
        self.SwitchStates = dict()
        self.master.update_idletasks()
    
    def _listControlsForSelectedPedal(self, selectedPedal):
        selectedPedalObject = self.AVAILABLE_PEDALS[selectedPedal]
        controls = selectedPedalObject.__dict__
        for item in controls.keys():
            self.Controls.append(controls[item])
                
    def _createControlsForSelectedPedal(self):
        for control in self.Controls:
            if isinstance(control, Switch):
                self.ControlItems[control.Name] = self._loadSwitchControl(control)
            elif isinstance(control, Knob):
                self.ControlItems[control.Name] = self._loadKnobControl(control)
            else:
                self.ControlItems[control.Name] = self._loadEditControl(control)
            self.ControlLabels[control.Name] = Label(self._controlsframe, text=control.Name, anchor="w", width=12)
    
    def _placeControls(self):
        row = 0
        for control in self.Controls:
            self.ControlLabels[control.Name].grid(column=0, row=row, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            self.ControlItems[control.Name].grid(column=1, row=row, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            row = row + 1
            
    def _loadKnobControl(self, modelcontrol):
        return Spinbox(self._controlsframe, from_=modelcontrol._min_value, to_=modelcontrol._max_value, width=10)
    
    def _loadSwitchControl(self, modelcontrol):
        switchframe = Frame(self._controlsframe)
        self.SwitchStates[modelcontrol.Name] = IntVar()
        on = Radiobutton(switchframe, text=modelcontrol._true_value, variable=self.SwitchStates[modelcontrol.Name], value=1)
        off = Radiobutton(switchframe, text=modelcontrol._false_value, variable=self.SwitchStates[modelcontrol.Name], value=2)
        on.pack(side="left")
        off.pack(side="left")
        return switchframe
        
    def _loadEditControl(self, modelcontrol):  
        return Entry(self._controlsframe, exportselection=False)      