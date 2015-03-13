'''
Created on Mar 13, 2015

@author: desposito
'''

class Knob(object):
    '''
    Generic knob object. Tracks name, min, max and current position.
    '''

    def __init__(self, name, min_value=0.0, max_value=10.0, current_position=0):
        '''
        Constructor
        '''
        self.Name = name
        self._min_value = min_value
        self._max_value = max_value
        self._validate_provided_position(current_position)
        self._current_position = current_position
        
    def Turn_To(self, new_position):
        '''
        Allows the knob to be set to a particular position.
        '''
        self._validate_provided_position(new_position)
        self._current_position = new_position
        
    def Current_Position(self):
        return self._current_position
        
    def _validate_provided_position(self, position):
        '''
        Ensures that the provided knob position is a valid number between the min and max value specified for the knob.
        '''
        try:
            position_value = float(position)
        except:
            raise TypeError("A non-numeric value was provided as the knob position. Value provided: {0}".format(position))
        
        if position_value < self._min_value or position_value > self._max_value:
            raise ValueError("The provided knob position is outside of the allowable range for this knob. Provided: {0} / Min: {1} / Max: {2}".format(position, self._min_value, self._max_value))
        
class Switch(object):
    '''
    Generic switch object.  Tracks name, on_value, off_value and current_state.
    '''
    
    def __init__(self, name, true_value="On", false_value="Off", current_state=True):
        '''
        Constructor
        '''
        self.Name = name
        self._true_value = true_value
        self._false_value = false_value
        self._current_state = current_state
        
    def Turn_On(self):
        '''
        Set the switch to the ON position.
        '''
        self._current_state = True
        
    def Turn_Off(self):
        '''
        Set the switch to the OFF position.
        '''
        self._current_state = False
        
    def Toggle(self):
        '''
        Set the switch to the state opposite of where it is.
        '''
        if self._current_state:
            self._current_state = False
        else:
            self._current_state = True
    
    def Current_State(self):
        '''
        Tell whether the switch is pressed or not.
        '''
        return self._current_state
    
    def Current_State_Name(self):
        '''
        Tell the name of the state based on whether the switch is pressed or not.
        '''
        if self._current_state:
            return self._true_value
        else:
            return self._false_value
        