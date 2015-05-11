'''
Created on Mar 18, 2015

@author: desposito
'''

from model.mics.mic import Mic
from model.utilities.controls import Switch


class MK319(Mic):
    '''Models the switches on the MK319 condenser mic based on the generic mic 
       model.
    '''

    def __init__(self, name, high_pass=False, pad=False):
        '''Constructor
        '''
        
        Mic.__init__(self, name)
        self.high_pass = Switch("High Pass", state=high_pass)
        self.pad = Switch("Pad", state=pad)
