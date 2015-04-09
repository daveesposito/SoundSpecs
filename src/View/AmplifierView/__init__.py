'''
Created on Apr 9, 2015

@author: desposito
'''
from Tkinter import Frame
from View.AmplifierView.CleanChannelView import CleanChannelView
from View.AmplifierView.DriveChannelView import DriveChannelView
from View.AmplifierView.MasterChannelView import MasterChannelView

class AmpflierView(Frame):
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.CleanView = CleanChannelView(self)
        self.DriveView = DriveChannelView(self)
        self.MasterView = MasterChannelView(self)
        
        self.CleanView.pack(expand=True, fill="both")
        self.DriveView.pack(expand=True, fill="both")
        self.MasterView.pack(expand=True, fill="both")