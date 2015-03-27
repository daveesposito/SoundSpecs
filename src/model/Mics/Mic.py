'''
Created on Mar 17, 2015

@author: desposito
'''

class Mic(object):
    '''
    Generic abstraction for how a mic will be used with focus on mic placement and position.
    '''

    names = list()

    def __init__(self, name):
        '''
        Constructor
        '''
        self.Name = name
        
        if name in self.names:
            raise ValueError("The specified name for this mic already exists. " + str(self.names))
        
        self.names.append(self.Name)
        self.Clock = None
        self.Radius = None
        self.XAngle = None
        self.YAngle = None
        self.Distance = None
        self.Placed = None
        
    def __del__(self):
        '''
        Handles removing the mic from the names list when the mic is destroyed.
        '''
        if self.Name in self.names:
            self.names.remove(self.Name)
        
    def Place_On_Amp(self, clock=12, radius=0, x_angle=0, y_angle=0, distance=0):
        '''
        Specifies where on the amp the mic has been placed.
        '''
        self._Set_Clock(clock)
        self._Set_Radius(radius)
        self._Set_XAngle(x_angle)
        self._Set_YAngle(y_angle)
        self._Set_Distance(distance)
        self.Placed = "Amp"
        
    def Place_In_Room(self, distance=60):
        '''
        Specifies how far from the center of the speaker cone the mic has been placed in the room.
        '''
        self.Clock = None
        self.Radius = None
        self.XAngle = None
        self.YAngle = None
        self._Set_Distance(distance)
        self.Placed = "Room"
        
    def Is_On_Amp(self):
        '''
        True if the mic has been placed on the amp. False if mic has NOT been placed on amp (does not imply it's been placed in room).
        '''
        if self.Placed == "Amp":
            return True
        else:
            return False
        
    def Is_In_Room(self):
        '''
        True if the mic has been placed in the room. False if mic has NOT been placed in room (DOES imply it's been placed on amp).
        '''
        if self.Placed == "Room":
            return True
        else:
            return False
        
    def Has_Been_Placed(self):
        '''
        True if mic has been placed.  False if it has not.
        '''
        if self.Placed is None:
            return False
        else:
            return True
        
    def Remove_From_Use(self):
        '''
        Removes a placed mic.
        '''
        self.Clock = None
        self.Radius = None
        self.XAngle = None
        self.YAngle = None
        self.Distance = None
        self.Placed = None
        
    def _Set_Attribute(self, new_val, min_allowed, max_allowed):
        '''
        Sets the Clock attribute with error checking.
        '''
        try:
            float_new_val = float(new_val)
        except:
            raise TypeError("Provided attribute must be able to convert to float. Provided value: " + str(new_val))
        
        if float_new_val < min_allowed or float_new_val > max_allowed:
            raise ValueError("Provided clock must be a value from " + str(min_allowed) + " to " + str(max_allowed) + ". Provided value: " + str(new_val))
        
        return float_new_val
    
    def _Set_Clock(self, new_clock):
        '''
        Sets limits on attribute value.
        '''
        self.Clock = self._Set_Attribute(new_clock, 1, 12)
        
    def _Set_Radius(self, new_radius):
        '''
        Sets limits on attribute value.
        '''
        self.Radius = self._Set_Attribute(new_radius, 0, 15)
    
    def _Set_XAngle(self, new_x):
        '''
        Sets limits on attribute value.
        '''
        self.XAngle = self._Set_Attribute(new_x, -90, 90)
        
    def _Set_YAngle(self, new_y):
        '''
        Sets limits on attribute value.
        '''
        self.YAngle = self._Set_Attribute(new_y, -90, 90)
    
    def _Set_Distance(self, new_distance):
        '''
        Sets limits on attribute value.
        '''
        self.Distance = self._Set_Attribute(new_distance, 0, 120)