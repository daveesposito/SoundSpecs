'''
Created on Mar 17, 2015

@author: desposito
'''
import unittest
from model.Utilities.Controls import Multiselect

class Test(unittest.TestCase):

    def test_ValidateBasicConstructor(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual(M1.Name, "Pickup Selector")
        self.assertEqual(M1.current_position, "Bridge")
        self.assertEqual(len(M1.selections), 2)
    
    def test_ConstructorWithNameNotInListRaisesException(self):
        self.assertRaises(ValueError, Multiselect, "Pickup Selector", "Middle", "Bridge", "Neck")
     
    def test_VerifyAllListItemsProvidedByConstructor(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertIn("Bridge", M1.selections)
        self.assertIn("Neck", M1.selections)
           
    def test_SetSelectionChoosesSpecifiedValue(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        for selection in M1.selections:
            M1.Set_Selection(selection)
            self.assertEqual(M1.current_position, selection)
        
    def test_SetSelectionWithInvalidEntryRaisesException(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, M1.Set_Selection, "Middle")
        
    def test_AddSelectionUpdatesListOfSelections(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertNotIn("Middle", M1.selections)
        M1.Add_Selection("Middle")
        self.assertIn("Middle", M1.selections)
        
    def test_AddingItemAlreadyInListRaisesException(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, M1.Add_Selection, "Bridge")
        
    def test_RemoveSelectionUpdatesListOfSelections(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertIn("Bridge", M1.selections)
        M1.Remove_Selection("Bridge")
        self.assertNotIn("Bridge", M1.selections)
        
    def test_RemovingItemNotInListRaisesException(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertRaises(ValueError, M1.Remove_Selection, "Middle")
        
    def test_CurrentPositionReturnsCorrectPosition(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual("Bridge", M1.Current_Position())
        M1.Set_Selection("Neck")
        self.assertEqual("Neck", M1.Current_Position())
        
    def test_ListOfOptionsReturnsCorrectList(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual(["Bridge", "Neck"], M1.List_Options())

    def test_NumberOfOptionsReturnsCorrectCount(self):
        M1 = Multiselect("Pickup Selector", "Bridge", "Bridge", "Neck")
        self.assertEqual(2, M1.Number_of_Options())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateBasicConstructor']
    unittest.main()