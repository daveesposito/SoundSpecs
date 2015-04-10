'''
Created on Apr 10, 2015

@author: desposito
'''
from Tkinter import Frame, Spinbox, Entry, Label, LabelFrame, Checkbutton,\
    BooleanVar

class ReAmpView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._raframe = LabelFrame(self.parent, text="ReAmp")
                
        self._ralevellabel = Label(self._raframe, text="Level", anchor="w")
        self._raliftlabel = Label(self._raframe, text="Ground Connection", anchor="w")
        self._raconnectionlabel = Label(self._raframe, text="Input", anchor="w")
        self.RALevel = Spinbox(self._raframe, from_=0, to_=10, width=10)
        self.RALiftState = BooleanVar()
        self.RALift = Checkbutton(self._raframe, text="Lifted", variable=self.RALiftState, anchor="w")
        self.RAConnection = Entry(self._raframe, exportselection=False)
        
        self._raframe.pack(expand=True, fill="both")
        
        self._raframe.columnconfigure(0, weight=1)
        self._raframe.columnconfigure(1, weight=1)
        
        self._ralevellabel.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._raliftlabel.grid(column=0, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._raconnectionlabel.grid(column=0, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.RALevel.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.RALift.grid(column=1, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.RAConnection.grid(column=1, row=2, sticky="n"+"e"+"w"+"s", padx=2, pady=2)