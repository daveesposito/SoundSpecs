'''
Created on Mar 17, 2015

@author: desposito
'''

import unittest

from model.Utilities.Controls import Multiselect


class Test(unittest.TestCase):


    def test_ValidateBasicConstructor(self):

        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual(multi.name, "Pickup Selector")
        self.assertEqual(multi.position, "Bridge")
        self.assertEqual(len(multi.selections), 2)
    
    def test_ConstructorWithNameNotInListRaisesException(self):
        
        self.assertRaises(ValueError, Multiselect, "Pickup Selector", 
                          "Middle", "Bridge", "Neck")
     
    def test_VerifyAllListItemsProvidedByConstructor(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertIn("Bridge", multi.selections)
        self.assertIn("Neck", multi.selections)
           
    def test_SetSelectionChoosesSpecifiedValue(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        for selection in multi.selections:
            multi.set_selection(selection)
            self.assertEqual(multi.position, selection)
        
    def test_SetSelectionWithInvalidEntryRaisesException(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, multi.set_selection, "Middle")
        
    def test_AddSelectionUpdatesListOfSelections(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertNotIn("Middle", multi.selections)
        multi.add_selection("Middle")
        self.assertIn("Middle", multi.selections)
        
    def test_AddingItemAlreadyInListRaisesException(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, multi.add_selection, "Bridge")
        
    def test_RemoveSelectionUpdatesListOfSelections(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertIn("Bridge", multi.selections)
        multi.remove_selection("Bridge")
        self.assertNotIn("Bridge", multi.selections)
        
    def test_RemovingItemNotInListRaisesException(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, multi.remove_selection, "Middle")
        
    def test_NumberOfOptionsReturnsCorrectCount(self):
        
        multi = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual(2, multi.number_of_options())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateBasicConstructor']
    unittest.main()
    
    