'''
Created on Mar 17, 2015

@author: desposito
'''

from model.utilities.controls import Knob, Multiselect


class SuzukiM():
    '''Models controls on the Suzuki M.
    '''
    

    def __init__(self, volume=10.0, bridge_tone=10.0, middle_tone=10.0, 
                 neck_tone=10.0, pickup="Bridge"):
        '''Constructor
        '''
        
        self.volume = Knob("Volume", current_position=volume)
        self.bridge_tone = Knob("Bridge Tone", current_position=bridge_tone)
        self.middle_tone = Knob("Middle Tone", current_position=middle_tone)
        self.neck_tone = Knob("Neck Tone", current_position=neck_tone)
        self.pickup = Multiselect("Pickup", pickup, "Bridge", "Bridge-Middle", 
                                  "Middle", "Middle-Neck", "Neck")
        