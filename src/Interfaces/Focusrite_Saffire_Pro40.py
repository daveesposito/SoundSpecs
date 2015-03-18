'''
Created on Mar 18, 2015

@author: desposito
'''


class Focusrite_Saffire_Pro40(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.AnalogInputs = list()
        for n in range(8):
            self.AnalogInputs.append(Input())
            if self.AnalogInputs[n] is None:
                raise IndexError("Unable to create input " + str(n))
        
class Input(object):
    '''
    classdocs
    '''
    
    def __init__(self, level=0.0, connected_device=None):
        '''
        constructor
        '''
        self.Level = level
        self.ConnectedDevice = connected_device