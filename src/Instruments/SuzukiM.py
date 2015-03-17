'''
Created on Mar 17, 2015

@author: desposito
'''
from Utilities.Controls import Knob, Multiselect
class SuzukiM(object):
    '''
    classdocs
    '''


    def __init__(self, volume=10.0, bridge_tone=10.0, middle_tone=10.0, neck_tone=10.0, pickup="Bridge"):
        '''
        Constructor
        '''
        self.Volume = Knob("Volume", current_position=volume)
        self.BridgeTone = Knob("Bridge Tone", current_position=bridge_tone)
        self.MiddleTone = Knob("Middle Tone", current_position=middle_tone)
        self.NeckTone = Knob("Neck Tone", current_position=neck_tone)
        self.Pickup = Multiselect("Pickup", pickup, "Bridge", "Bridge-Middle", "Middle", "Middle-Neck", "Neck")