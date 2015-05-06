'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame, LabelFrame, Spinbox, Radiobutton, IntVar, Label
from model.amplifier import drivechannel.DriveChannel

class DriveChannelView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        model = drivechannel()
        
        self._labelframe = LabelFrame(self.parent, text="Drive Channel")
        self._gainlabel = Label(self._labelframe, text="Gain", anchor="w")
        self._basslabel = Label(self._labelframe, text="Bass", anchor="w")
        self._midlabel = Label(self._labelframe, text="Mid", anchor="w")
        self._treblelabel = Label(self._labelframe, text="Treble", anchor="w")
        self._contourlabel = Label(self._labelframe, text="Contour", anchor="w")
        self._volumelabel = Label(self._labelframe, text="Volume", anchor="w")
        self.Gain = Spinbox(self._labelframe, from_=model.Gain._min_value, to_=model.Gain._max_value)
        self.Bass = Spinbox(self._labelframe, from_=model.Bass._min_value, to_=model.Bass._max_value)
        self.Mid = Spinbox(self._labelframe, from_=model.Mid._min_value, to_=model.Mid._max_value)
        self.Treble = Spinbox(self._labelframe, from_=model.Treble._min_value, to_=model.Treble._max_value)
        self.Contour = Spinbox(self._labelframe, from_=model.Contour._min_value, to_=model.Contour._max_value)
        self.Volume = Spinbox(self._labelframe, from_=model.Volume._min_value, to_=model.Volume._max_value)
        
        self._typelabel = Label(self._labelframe, text="Drive Type", anchor="w")
        self.Drive_Type = IntVar()
        self.Drive_OD1 = Radiobutton(self._labelframe, text=model.DriveType._true_value, variable=self.Drive_Type, value=1)
        self.Drive_OD2 = Radiobutton(self._labelframe, text=model.DriveType._false_value, variable=self.Drive_Type, value=2)
        
        self._labelframe.pack(expand=True, fill="both", padx=2, pady=2)
        
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.columnconfigure(2, weight=1)
        self._labelframe.columnconfigure(3, weight=1)
        
        self._gainlabel.grid(column=0, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._basslabel.grid(column=0, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._midlabel.grid(column=0, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._treblelabel.grid(column=0, row=3, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._contourlabel.grid(column=0, row=4, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._volumelabel.grid(column=0, row=5, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self.Gain.grid(column=2, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Bass.grid(column=2, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Mid.grid(column=2, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Treble.grid(column=2, row=3, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Contour.grid(column=2, row=4, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Volume.grid(column=2, row=5, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self._typelabel.grid(column=0, row=6, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Drive_OD1.grid(column=2, row=6, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Drive_OD2.grid(column=3, row=6, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        