'''
Created on Apr 10, 2015

@author: desposito
'''
from Tkinter import Frame, Spinbox, Entry, Label, LabelFrame

class DIView(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self._diframe = LabelFrame(self.parent, text="IMP2")
                
        self._dilevellabel = Label(self._diframe, text="Level", anchor="w")
        self._diconnectionlabel = Label(self._diframe, text="Input", anchor="w")
        self.DILevel = Spinbox(self._diframe, from_=0, to_=10, width=10)
        self.DIConnection = Entry(self._diframe, exportselection=False)
        
        self._diframe.pack(expand=True, fill="both")
        
        self._diframe.columnconfigure(0, weight=1)
        self._diframe.columnconfigure(1, weight=1)
        
        self._dilevellabel.grid(column=0, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self._diconnectionlabel.grid(column=0, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.DILevel.grid(column=1, row=0, sticky="n"+"e"+"w"+"s", padx=2, pady=2)
        self.DIConnection.grid(column=1, row=1, sticky="n"+"e"+"w"+"s", padx=2, pady=2)