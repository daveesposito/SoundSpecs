'''
Created on Mar 27, 2015

@author: desposito
'''

class SignalChain(object):
    '''
    Provides functionality for creating signal chain parameters including all equipment involved in the chain.
    '''
    
    def __init__(self):
        '''
        Constructor 
        '''
        self.Instrument = None
        self.Pedals = list()
        self.DI = None
        self.Reamp = None
        self.Amp = None
        self.Input = None