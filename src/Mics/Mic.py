'''
Created on Mar 17, 2015

@author: desposito
'''

class Mic(object):
    '''
    classdocs
    '''

    names = list()

    def __init__(self, name="SM57"):
        '''
        Constructor
        '''
        if name in self.names:
            raise ValueError("The specified name for this mic already exists.")
        
        self.Name = name
        self.names.append(self.name)
        self.Clock = None
        self.Radius = None
        self.XAngle = None
        self.YAngle = None
        self.Distance = None
        
    def Place_On_Amp(self, clock=12, radius=0, x_angle=0, y_angle=0, distance=0):
        '''
        Specifies where on the amp the mic has been placed.
        '''
        try:
            clock_val = int(clock)
        except:
            raise TypeError("Provided clock must be able to convert to integer. Provided value: " + str(clock))
        
        if clock_val < 1 or clock_val > 12:
            raise ValueError("Provided clock must be a value from 1 to 12. Provided value: " + str(clock))
        
        try:
            radius_val = float(radius)
        except:
            raise TypeError("Provided radius must be able to convert to float. Provided value: " + str(radius))
        
        if radius_val < 0:
            raise ValueError("Provided radius must be positive value from center of speaker cone. Provided value: " + str(radius))
        
        try:
            x_angle_val = float(x_angle)
        except:
            raise TypeError("Provided X Angle must be able to convert to float. Provided value: " + str(x_angle))
        
        if x_angle_val < -90 or x_angle_val > 90:
            raise ValueError("Provided X Angle must be a value from -90 to 90. Provided value: " + str(x_angle))
        
        try:
            y_angle_val = float(y_angle)
        except:
            raise TypeError("Provided Y Angle must be able to convert to float. Provided value: " + str(y_angle))
        
        if y_angle_val < -90 or y_angle_val > 90:
            raise ValueError("Provided Y Angle must be a value from -90 to 90. Provided value: " + str(y_angle))
        
        try:
            distance_val = float(distance)
        except:
            raise TypeError("Provided Distance must be able to convert to float. Provided value: " + str(distance))
        
        if distance_val < -90 or distance_val > 90:
            raise ValueError("Provided Distance must be a value from -90 to 90. Provided value: " + str(distance))
        
        self.Clock = clock_val
        self.Radius = radius_val
        self.XAngle = x_angle_val
        self.YAngle = y_angle_val
        self.Distance = distance_val
        
    def Place_In_Room(self, distance):
        '''
        Specifies how far from the center of the speaker cone the mic has been placed in the room.
        '''
        try:
            distance_val = float(distance)
        except:
            raise TypeError("Provided Distance must be able to convert to float. Provided value: " + str(distance))
        
        if distance_val < -90 or distance_val > 90:
            raise ValueError("Provided Distance must be a value from -90 to 90. Provided value: " + str(distance))
        
        self.Clock = None
        self.Radius = None
        self.XAngle = None
        self.YAngle = None
        self.Distance = distance_val
        
    def Is_On_Amp(self):
        '''
        True if the mic has been placed on the amp. False if mic has NOT been placed on amp (does not imply it's been placed in room).
        '''
        if not self.Clock is None:
            return True
        else:
            return False
        
    def Is_In_Room(self):
        '''
        True if the mic has been placed in the room. False if mic has NOT been placed in room (DOES imply it's been placed on amp).
        '''
        if self.Clock is None and not self.Distance is None:
            return True
        else:
            return False
        
    def Has_Been_Placed(self):
        '''
        True if mic has been placed.  False if it has not.
        '''
        if self.Clock is None and self.Distance is None:
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