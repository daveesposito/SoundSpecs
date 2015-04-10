'''
Created on Apr 10, 2015

@author: desposito
'''
from Tkinter import Frame, LabelFrame, Label, Spinbox, Entry, Checkbutton, BooleanVar

class Focusrite_InputView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._labelframe = LabelFrame(self.parent, text="Focusrite Saffire Pro40 - Input Channel")
        
        self._channellalbel = Label(self._labelframe, text="Channel", anchor="w")
        self._levellabel = Label(self._labelframe, text="Level", anchor="w")
        self._connectionlabel = Label(self._labelframe, text="Input", anchor="w")
        self._instrumentlevellabel = Label(self._labelframe, text="Instrument Level", anchor="w")
        self._padlabel = Label(self._labelframe, text="Pad", anchor="w")
        
        self.Channel = Spinbox(self._labelframe, from_=1, to_=8, width=10, command=self.checkChannels)
        self.Level = Spinbox(self._labelframe, from_=0, to_=10, width=10)
        self.Connection = Entry(self._labelframe, exportselection=True)
        self.InstrumentLevelState = BooleanVar()
        self.InstrumentLevel = Checkbutton(self._labelframe, text="Active", variable=self.InstrumentLevelState, anchor="w")
        self.PadState = BooleanVar()
        self.Pad = Checkbutton(self._labelframe, text="Active", variable=self.PadState, anchor="w")
        
        self._labelframe.pack(expand=True, fill="both")
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        
        self._channellalbel.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._levellabel.grid(column=0, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._connectionlabel.grid(column=0, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._instrumentlevellabel.grid(column=0, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._padlabel.grid(column=0, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self.Channel.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Level.grid(column=1, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Connection.grid(column=1, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.InstrumentLevel.grid(column=1, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Pad.grid(column=1, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
    def checkChannels(self):
        currentChannel = self.Channel.get()
        if currentChannel == '1' or currentChannel == '2':
            self._instrumentlevellabel.grid(column=0, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            self._padlabel.grid(column=0, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            self.InstrumentLevel.grid(column=1, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
            self.Pad.grid(column=1, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        else:
            self._instrumentlevellabel.grid_forget()
            self._padlabel.grid_forget()
            self.InstrumentLevel.grid_forget()
            self.Pad.grid_forget()