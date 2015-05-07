'''
Created on Mar 13, 2015

@author: desposito
'''


class Knob():
    ''' Generic knob object. Tracks name, min, max and current position.
    '''


    def __init__(self, name, min_value=0.0, max_value=10.0, 
                 current_position=0):
        '''Constructor
        '''

        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        
        self._validate_position(current_position)
        self.current_position = current_position
        
    def turn_to(self, new_position):
        '''Allows the knob to be set to a particular position.
        '''
        
        self._validate_position(new_position)
        self.current_position = new_position
        
    def _validate_position(self, position):
        '''Ensures that the provided knob position is a valid number between 
           the min and max value specified for the knob.
        '''
        
        try:
            position_val = float(position)
        except:
            raise TypeError("Non-numeric value provided: {0}".format(position))
        
        if position_val < self.min_value or position_val > self.max_value:
            raise ValueError("Bad value: {0} / Min: {1} / Max: {2}"\
                             .format(position, self.min_value, self.max_value))

        
class Switch():    
    '''Generic switch object.  Tracks name, on_val, off_val and state.
    '''
    
    
    def __init__(self, name, true_val="On", false_val="Off", state=True):
        '''Constructor
        '''
        
        self.name = name
        self._true_value = true_val
        self._false_value = false_val
        self.state = state
        
    def turn_on(self):
        '''Set the switch to the ON position.
        '''
        
        self.state = True
        
    def turn_off(self):
        '''Set the switch to the OFF position.
        '''
        
        self.state = False
        
    def toggle(self):
        '''Set the switch to the state opposite of where it is.
        '''
        
        if self.state:
            self.state = False
        else:
            self.state = True
    
    def state_name(self):
        '''Tell the name of the state based on whether the switch is pressed 
           or not.
        '''
        
        if self.state:
            return self._true_value
        else:
            return self._false_value
        
        
class Multiselect():
    '''Multiselect switch useful for things like guitar pickup selectors.
    '''
    
    
    def __init__(self, name, position, *selections):
        '''Constructor
        '''
        
        self.name = name
        self.position = ""
        
        self.selections = list()
        for selection in selections:
            try:
                selection_string = str(selection)
            except:
                raise TypeError("selection must be representable as a string.")
            self.selections.append(selection_string)
        
        self.set_selection(position)
        
    def set_selection(self, new_selection):
        '''Set a new position for the switch.
        '''
        
        if new_selection not in self.selections:
            raise ValueError("Provided position not valid: {0}"\
                             .format(str(new_selection)))
        
        self.position = new_selection
        
    def add_selection(self, new_selection):
        '''Adds a value to the valid list of selections.
        '''
        
        if new_selection in self.selections:
            raise ValueError("selection already exists: {0}"\
                             .format(str(new_selection)))
        
        self.selections.append(new_selection)
        
    def remove_selection(self, selection_to_remove):
        '''Remove a selection from the list of selections.
        '''
        
        if selection_to_remove not in self.selections:
            raise ValueError("Provided selection doesn't exist: {0}"\
                             .format((selection_to_remove)))
        
        self.selections.remove(selection_to_remove)
    
    def number_of_options(self):
        '''Returns the number of available options.
        '''
        
        return len(self.selections)
    