'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame, LabelFrame, Spinbox, Radiobutton, IntVar, Label
from model.amplifier import masterchannel.MasterChannel

class MasterChannelView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        model = masterchannel()
        
        self._labelframe = LabelFrame(self.parent, text="Master Channel")
        self._volumelabel = Label(self._labelframe, text="Volume", anchor="w")
        self._reverblabel = Label(self._labelframe, text="Reverb", anchor="w")
        self._sendlevellabel = Label(self._labelframe, text="Send Level", anchor="w")
        self.Volume = Spinbox(self._labelframe, from_=model.Volume._min_value, to_=model.Volume._max_value)
        self.Reverb = Spinbox(self._labelframe, from_=model.Reverb._min_value, to_=model.Reverb._max_value)
        self.SendLevel = Spinbox(self._labelframe, from_=model.Send_Level._min_value, to_=model.Send_Level._max_value)
                
        self._channelselectlabel = Label(self._labelframe, text="Channel Select", anchor="w")
        self.Selected_Channel = IntVar()
        self.Select_Clean = Radiobutton(self._labelframe, text=model.ChannelSelect._true_value, variable=self.Selected_Channel, value=1)
        self.Select_Drive = Radiobutton(self._labelframe, text=model.ChannelSelect._false_value, variable=self.Selected_Channel, value=2)
        
        self._labelframe.pack(expand=True, fill="both", padx=2, pady=2)
        
        self._labelframe.columnconfigure(0, weight=1)
        self._labelframe.columnconfigure(1, weight=1)
        self._labelframe.columnconfigure(2, weight=1)
        self._labelframe.columnconfigure(3, weight=1)
        
        self._volumelabel.grid(column=0, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._reverblabel.grid(column=0, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._sendlevellabel.grid(column=0, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
                
        self.Volume.grid(column=2, row=0, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Reverb.grid(column=2, row=1, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.SendLevel.grid(column=2, row=2, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        
        self._channelselectlabel.grid(column=0, row=3, columnspan=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Select_Clean.grid(column=2, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.Select_Drive.grid(column=3, row=3, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        