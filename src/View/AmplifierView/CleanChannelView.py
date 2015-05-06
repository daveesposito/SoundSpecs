'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame, LabelFrame, Spinbox, Radiobutton, IntVar, Label
from model.amplifier import cleanchannel.CleanChannel

class CleanChannelView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        model = cleanchannel()
        
        self._labelframe = LabelFrame(self.parent, text="Clean Channel")
        self._gainlabel = Label(self._labelframe, text="Gain", anchor="w")
        self._basslabel = Label(self._labelframe, text="Bass", anchor="w")
        self._midlabel = Label(self._labelframe, text="Mid", anchor="w")
        self._treblelabel = Label(self._labelframe, text="Treble", anchor="w")
        self.Gain = Spinbox(self._labelframe, from_=model.Gain._min_value, to_=model.Gain._max_value)
        self.Bass = Spinbox(self._labelframe, from_=model.Bass._min_value, to_=model.Bass._max_value)
        self.Mid = Spinbox(self._labelframe, from_=model.Mid._min_value, to_=model.Mid._max_value)
        self.Treble = Spinbox(self._labelframe, from_=model.Treble._min_value, to_=model.Treble._max_value)
        
        self._typelabel = Label(self._labelframe, text="Clean Type", anchor="w")
        self.Clean_Type = IntVar()
        self.Clean_Crunch = Radiobutton(self._labelframe, text=model.CleanType._true_value, variable=self.Clean_Type, value=1)
        self.Clean_Clean = Radiobutton(self._labelframe, text=model.CleanType._false_value, variable=self.Clean_Type, value=2)
        
        self._labelframe.pack(expand=True, fill="both", padx=2, pady=2)
        
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.columnconfigure(2, weight=1)
        self._labelframe.columnconfigure(3, weight=1)
        
        self._gainlabel.grid(column=0, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._basslabel.grid(column=0, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._midlabel.grid(column=0, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._treblelabel.grid(column=0, row=3, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self.Gain.grid(column=2, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Bass.grid(column=2, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Mid.grid(column=2, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Treble.grid(column=2, row=3, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self._typelabel.grid(column=0, row=4, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Clean_Clean.grid(column=2, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Clean_Crunch.grid(column=3, row=4, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        