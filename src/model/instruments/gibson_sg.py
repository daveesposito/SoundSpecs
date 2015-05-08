'''
Created on Mar 17, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Multiselect


class GibsonSG():
    '''Models controls on the Gibson SG Special.
    '''


    def __init__(self, bridge_volume=10.0, bridge_tone=10.0, neck_volume=10.0, 
                 neck_tone=10.0, pickup="Bridge"):
        '''Constructor
        '''
        
        self.bridge_vol = Knob("Bridge Volume", current_position=bridge_volume)
        self.bridge_tone = Knob("Bridge Tone", current_position=bridge_tone)
        self.neck_vol = Knob("Neck Volume", current_position=neck_volume)
        self.neck_tone = Knob("Neck Tone", current_position=neck_tone)
        self.pickup = Multiselect("Pickup", pickup, "Bridge", "Bridge-Neck", 
                                  "Neck")