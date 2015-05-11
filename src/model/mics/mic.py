'''
Created on Mar 17, 2015

@author: desposito
'''


class Mic():
    '''Generic abstraction for how a mic will be used with focus on mic 
       placement and position.
    '''


    names = list()

    def __init__(self, name):
        '''Constructor
        '''
        
        self.name = name
                
        if name in self.names:
            raise ValueError("Provided name already exists. {0}".\
                             format(self.names))
        
        self.names.append(self.name)
        
        self.clock = None
        self.radius = None
        self.x_angle = None
        self.y_angle = None
        self.distance = None
        self.placed = None
        
    def __del__(self):
        '''Handles removing the mic from the names list when the mic is 
           destroyed.
        '''
        
        if self.name in self.names:
            self.names.remove(self.name)
        
    def place_on_amp(self, clock=12, radius=0, x_angle=0, y_angle=0, 
                     distance=0):
        '''Specifies where on the amp the mic has been placed.
        '''
        
        self._set_clock(clock)
        self._set_radius(radius)
        self._set_x_angle(x_angle)
        self._set_y_angle(y_angle)
        self._set_distance(distance)
        self.placed = "Amp"
        
    def place_in_room(self, distance=60):
        '''Specifies how far from the center of the speaker cone the mic has 
           been placed in the room.
        '''
        
        self.clock = None
        self.radius = None
        self.x_ngle = None
        self.y_angle = None
        self._set_distance(distance)
        self.placed = "Room"
        
    def is_on_amp(self):
        '''True if the mic has been placed on the amp. False if mic has NOT 
           been placed on amp (does not imply it's been placed in room).
        '''
        
        if self.placed == "Amp":
            return True
        else:
            return False
        
    def is_in_room(self):
        '''True if the mic has been placed in the room. False if mic has NOT 
           been placed in room (DOES imply it's been placed on amp).
        '''
        
        if self.placed == "Room":
            return True
        else:
            return False
        
    def has_been_placed(self):
        '''True if mic has been placed.  False if it has not.
        '''
        
        if self.placed is None:
            return False
        else:
            return True
        
    def remove_from_use(self):
        '''Removes a placed mic.
        '''
        
        self.clock = None
        self.radius = None
        self.x_angle = None
        self.y_angle = None
        self.distance = None
        self.placed = None
        
    def _set_attribute(self, new_val, min_allowed, max_allowed):
        '''Sets the Clock attribute with error checking.
        '''
        
        try:
            float_new_val = float(new_val)
        except:
            raise TypeError("new_val not float: {0}".format(new_val))
        
        if float_new_val < min_allowed or float_new_val > max_allowed:
            raise ValueError("Must be betwen {0} and {1}"\
                             .format(min_allowed, max_allowed))
        
        return float_new_val
    
    def _set_clock(self, new_clock):
        '''Sets limits on attribute value.
        '''
        
        self.clock = self._set_attribute(new_clock, 1, 12)
        
    def _set_radius(self, new_radius):
        '''Sets limits on attribute value.
        '''
        
        self.radius = self._set_attribute(new_radius, 0, 15)
    
    def _set_x_angle(self, new_x):
        '''Sets limits on attribute value.
        '''
        
        self.x_angle = self._set_attribute(new_x, -90, 90)
        
    def _set_y_angle(self, new_y):
        '''Sets limits on attribute value.
        '''
        
        self.y_angle = self._set_attribute(new_y, -90, 90)
    
    def _set_distance(self, new_distance):
        '''Sets limits on attribute value.
        '''
        
        self.distance = self._set_attribute(new_distance, 0, 120)
        