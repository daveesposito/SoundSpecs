'''
Created on Apr 8, 2015

@author: desposito
'''
from Tkinter import Frame, Listbox, LabelFrame, Spinbox, Label, IntVar, Radiobutton

class MicView(Frame):
    '''
    Provides a frame to select the instrument and instrument parameters for the signal chain.
    '''

    AVAILABLE_MICS = ['SM57',
                      'MK319',
                      '<none>']

    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._labelframe = LabelFrame(self.parent, text="Select Mic")
        self.MicList = Listbox(self._labelframe, selectmode="single", height=len(self.AVAILABLE_MICS))
        self._controlsframe = Frame(self._labelframe, width=173, height=125)
        self._placedframe = Frame(self._controlsframe)
        self._padframe = Frame(self._controlsframe)
        self._highpassframe = Frame(self._controlsframe)
        
        self._placedlabel = Label(self._controlsframe, text="Placed", anchor="w")
        self._clocklabel = Label(self._controlsframe, text="Clock", anchor="w")
        self._radiuslabel = Label(self._controlsframe, text="Radius", anchor="w")
        self._xanglelabel = Label(self._controlsframe, text="X Angle", anchor="w")
        self._yanglelabel = Label(self._controlsframe, text="Y Angle", anchor="w")
        self._distancelabel = Label(self._controlsframe, text="Distance", anchor="w")
        self._padlabel = Label(self._controlsframe, text="Pad", anchor="w")
        self._highpasslabel = Label(self._controlsframe, text="Highpass", anchor="w")
        
        self.Clock = Spinbox(self._controlsframe, from_=1, to_=12, width=10)
        self.Radius = Spinbox(self._controlsframe, from_=0, to_=15, width=10)
        self.XAngle = Spinbox(self._controlsframe, from_=-90, to_=90, width=10)
        self.YAngle = Spinbox(self._controlsframe, from_=-90, to_=90, width=10)
        self.Distance = Spinbox(self._controlsframe, from_=0, to_=120, width=10)
        self.Placed_State = IntVar()
        self.Placed_Amp = Radiobutton(self._placedframe, text="Amp", variable=self.Placed_State, value=1, command=self._updateControlsForPlacement)
        self.Placed_Room = Radiobutton(self._placedframe, text="Room", variable=self.Placed_State, value=2, command=self._updateControlsForPlacement)
        self.Placed_Amp.pack(side="left")
        self.Placed_Room.pack(side="left")
        self.Pad_State = IntVar()
        self.Pad_None = Radiobutton(self._padframe, text="None", variable=self.Pad_State, value=1)
        self.Pad_10dB = Radiobutton(self._padframe, text="-10dB", variable=self.Pad_State, value=2)
        self.Pad_None.pack(side="left")
        self.Pad_10dB.pack(side="left")        
        self.Highpass_State = IntVar()
        self.Highpass_Off = Radiobutton(self._highpassframe, text="Off", variable=self.Highpass_State, value=1)
        self.Highpass_On = Radiobutton(self._highpassframe, text="On", variable=self.Highpass_State, value=2)
        self.Highpass_Off.pack(side="left")
        self.Highpass_On.pack(side="left")
        
        for mic in self.AVAILABLE_MICS:
            self.MicList.insert("end", mic)
            
        self.MicList.bind('<<ListboxSelect>>', self.loadSwitches)
            
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.rowconfigure(0, weight=1)
        self._labelframe.pack(expand=True, fill="both")
        self.MicList.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._controlsframe.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self._controlsframe.columnconfigure(0, weight=1)
        self._controlsframe.columnconfigure(1, weight=1)
        
        self._placedlabel.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._clocklabel.grid(column=0, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._radiuslabel.grid(column=0, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._xanglelabel.grid(column=0, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._yanglelabel.grid(column=0, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._distancelabel.grid(column=0, row=5, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self._placedframe.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Clock.grid(column=1, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Radius.grid(column=1, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.XAngle.grid(column=1, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.YAngle.grid(column=1, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Distance.grid(column=1, row=5, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
    def loadSwitches(self, evt):
        selectedMic = self.MicList.selection_get()
        if selectedMic != ():
            if selectedMic == 'MK319':
                self._loadControls()
            else:
                self._clearControls()
    
    def _clearControls(self):
        self._padlabel.grid_forget()
        self._highpasslabel.grid_forget()
        self._padframe.grid_forget()
        self._highpassframe.grid_forget()
            
    def _loadControls(self):
        self._padlabel.grid(column=0, row=6, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._highpasslabel.grid(column=0, row=7, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._padframe.grid(column=1, row=6, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._highpassframe.grid(column=1, row=7, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
    def _updateControlsForPlacement(self):
        if self.Placed_State.get() == 1:
            self._enableAmpStates()
        else:
            self._disableAmpStates()
            
    def _enableAmpStates(self):
        self.Clock.config(state="normal")
        self.Radius.config(state="normal")
        self.XAngle.config(state="normal")
        self.YAngle.config(state="normal")
        
    def _disableAmpStates(self):
        self.Clock.config(state="disabled")
        self.Radius.config(state="disabled")
        self.XAngle.config(state="disabled")
        self.YAngle.config(state="disabled")