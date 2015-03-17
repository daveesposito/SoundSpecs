'''
Created on Mar 17, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Multiselect

class GibsonLesPaul(object):
    '''
    classdocs
    '''

    def __init__(self, bridge_volume=10.0, bridge_tone=10.0, neck_volume=10.0, neck_tone=10.0, pickup="Bridge"):
        '''
        Constructor
        '''
        self.BridgeVolume = Knob("Bridge Volume", current_position=bridge_volume)
        self.BridgeTone = Knob("Bridge Tone", current_position=bridge_tone)
        self.NeckVolume = Knob("Neck Volume", current_position=neck_volume)
        self.NeckTone = Knob("Neck Tone", current_position=neck_tone)
        self.Pickup = Multiselect("Pickup", pickup, "Bridge", "Bridge-Neck", "Neck")