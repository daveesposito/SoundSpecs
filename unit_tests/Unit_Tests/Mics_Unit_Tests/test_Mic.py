'''
Created on Mar 18, 2015

@author: desposito
'''

import unittest

from model.mics.mic import Mic


class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        
        mic = Mic("SM57A")
        self.assertEqual(mic.name, "SM57A")
        self.assertIn("SM57A", mic.names)
        self.assertIsNone(mic.clock)
        self.assertIsNone(mic.radius)
        self.assertIsNone(mic.x_angle)
        self.assertIsNone(mic.y_angle)
        self.assertIsNone(mic.distance)
        self.assertIsNone(mic.placed)
        
    def test_MultipleObjectsTrackSameListOfNames(self):
        mic = Mic("SM57A")
        M2 = Mic("SM57B")
        self.assertEqual(mic.names, M2.names)
        
    def test_CannotUseDuplicateNames(self):
        mic = Mic("SM57A")
        self.assertEqual(mic.name, "SM57A")
        self.assertRaises(ValueError, Mic, "SM57A")

    def test_SetAttributeReturnsValueAfterPassingValidations(self):
        mic = Mic("SM57A")
        value = mic._set_attribute(3.14, 0, 5)
        self.assertEqual(value, 3.14)
        
    def test_SetAttributePassesWhenSuppliedAnInteger(self):
        mic = Mic("SM57A")
        value = mic._set_attribute(3, 0, 5)
        self.assertEqual(value, 3)
        
    def test_SetAttributeWithNonNumericRaisesException(self):
        mic = Mic("SM57A")
        self.assertRaises(TypeError, mic._set_attribute, "dog", 0, 5)
        
    def test_SetAttributeWithLowLimitErrorRaisesException(self):
        mic = Mic("SM57A")
        self.assertRaises(ValueError, mic._set_attribute, -2, 0, 5)
        
    def test_SetAttributeWithHighLimitErrorRaisesException(self):
        mic = Mic("SM57A")
        self.assertRaises(ValueError, mic._set_attribute, 10, 0, 5)
        
    def test_SetAttributeAllowsNegativeNumbers(self):
        mic = Mic("SM57A")
        value = mic._set_attribute(-5, -10, -1)
        self.assertEqual(value, -5)
        
    def test_SetclockUpdatesclockAttribute(self):
        mic = Mic("SM57A")
        mic._set_clock(3)
        self.assertEqual(mic.clock, 3)
    
    def test_MinimumclockIs1(self):
        mic = Mic("SM57A")
        mic._set_clock(1)
        self.assertEqual(mic.clock, 1)
        self.assertRaises(ValueError, mic._set_clock, 0)
        
    def test_MaximumclockIs12(self):
        mic = Mic("SM57A")
        mic._set_clock(12)
        self.assertEqual(mic.clock, 12)
        self.assertRaises(ValueError, mic._set_clock, 13)
        
    def test_SetradiusUpdatesradiusAttribute(self):
        mic = Mic("SM57A")
        mic._set_radius(5)
        self.assertEqual(mic.radius, 5)
    
    def test_MinimumradiusIs0(self):
        mic = Mic("SM57A")
        mic._set_radius(0)
        self.assertEqual(mic.radius, 0)
        self.assertRaises(ValueError, mic._set_radius, -1)
        
    def test_MaximumradiusIs15(self):
        mic = Mic("SM57A")
        mic._set_radius(15)
        self.assertEqual(mic.radius, 15)
        self.assertRaises(ValueError, mic._set_radius, 16)    
    
    def test_Setx_angleUpdatesx_angleAttribute(self):
        mic = Mic("SM57A")
        mic._set_x_angle(-80)
        self.assertEqual(mic.x_angle, -80)
        
    def test_Minimumx_angleIsMinus90(self):
        mic = Mic("SM57A")
        mic._set_x_angle(-90)
        self.assertEqual(mic.x_angle, -90)
        self.assertRaises(ValueError, mic._set_x_angle, -91)
    
    def test_Maximumx_angleIs90(self):
        mic = Mic("SM57A")
        mic._set_x_angle(90)
        self.assertEqual(mic.x_angle, 90)
        self.assertRaises(ValueError, mic._set_x_angle, 91)
        
    def test_Sety_angleUpdatesy_angleAttribute(self):
        mic = Mic("SM57A")
        mic._set_y_angle(89)
        self.assertEqual(mic.y_angle, 89)
        
    def test_Minimumy_angleIsMinus90(self):
        mic = Mic("SM57A")
        mic._set_y_angle(-90)
        self.assertEqual(mic.y_angle, -90)
        self.assertRaises(ValueError, mic._set_y_angle, -91)
    
    def test_Maximumy_angleIs90(self):
        mic = Mic("SM57A")
        mic._set_y_angle(90)
        self.assertEqual(mic.y_angle, 90)
        self.assertRaises(ValueError, mic._set_y_angle, 91)
        
    def test_SetdistanceUpdatesdistanceAttribute(self):
        mic = Mic("SM57A")
        mic._set_distance(76)
        self.assertEqual(mic.distance, 76)
        
    def test_MinimumdistanceIs0(self):
        mic = Mic("SM57A")
        mic._set_distance(0)
        self.assertEqual(mic.distance, 0)
        self.assertRaises(ValueError, mic._set_distance, -1)
    
    def test_MaximumdistanceIs120(self):
        mic = Mic("SM57A")
        mic._set_distance(120)
        self.assertEqual(mic.distance, 120)
        self.assertRaises(ValueError, mic._set_distance, 121)
    
    def test_PlaceOnAmpDefaultValues(self):
        mic = Mic("SM57A")
        mic.place_on_amp()
        self.assertEqual(mic.clock, 12)
        self.assertEqual(mic.radius, 0)
        self.assertEqual(mic.x_angle, 0)
        self.assertEqual(mic.y_angle, 0)
        self.assertEqual(mic.distance, 0)
        self.assertEqual(mic.placed, "Amp")
        
    def test_PlaceOnAmpWithclock(self):
        mic = Mic("SM57A")
        mic.place_on_amp(clock=6)
        self.assertEqual(mic.clock, 6)
        
    def test_PlaceOnAmpWithradius(self):
        mic = Mic("SM57A")
        mic.place_on_amp(radius=6)
        self.assertEqual(mic.radius, 6)
        
    def test_PlaceOnAmpWithx_angle(self):
        mic = Mic("SM57A")
        mic.place_on_amp(x_angle=6)
        self.assertEqual(mic.x_angle, 6)
    
    def test_PlaceOnAmpWithy_angle(self):
        mic = Mic("SM57A")
        mic.place_on_amp(y_angle=6)
        self.assertEqual(mic.y_angle, 6)
        
    def test_PlaceOnAmpWithdistance(self):
        mic = Mic("SM57A")
        mic.place_on_amp(distance=6)
        self.assertEqual(mic.distance, 6)
        
    def test_PlaceInRoomDefaultValues(self):
        mic = Mic("SM57A")
        mic.place_in_room()
        self.assertIsNone(mic.clock)
        self.assertIsNone(mic.radius)
        self.assertIsNone(mic.x_angle)
        self.assertIsNone(mic.y_angle)
        self.assertEqual(mic.distance, 60)
        self.assertEqual(mic.placed, "Room")
        
    def test_PlaceInRoomWithdistance(self):
        mic = Mic("SM57A")
        mic.place_in_room(36)
        self.assertEqual(mic.distance, 36)
        
    def test_RemoveMicFromAmp(self):
        mic = Mic("SM57A")
        mic.place_on_amp()
        self.assertEqual(mic.placed, "Amp")
        mic.remove_from_use()
        self.assertIsNone(mic.clock)
        self.assertIsNone(mic.radius)
        self.assertIsNone(mic.x_angle)
        self.assertIsNone(mic.y_angle)
        self.assertIsNone(mic.distance)
        self.assertIsNone(mic.placed)
        
    def test_RemoveMicFromRoom(self):
        mic = Mic("SM57A")
        mic.place_in_room()
        self.assertEqual(mic.placed, "Room")
        mic.remove_from_use()
        self.assertIsNone(mic.clock)
        self.assertIsNone(mic.radius)
        self.assertIsNone(mic.x_angle)
        self.assertIsNone(mic.y_angle)
        self.assertIsNone(mic.distance)
        self.assertIsNone(mic.placed)
        
    def test_IsOnAmpNewToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        
    def test_IsOnAmpRoomToAmp(self):
        mic = Mic("SM57A")
        mic.place_in_room()
        self.assertFalse(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        
    def test_IsOnAmpAmpToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        mic.place_in_room()
        self.assertFalse(mic.is_on_amp())
        
    def test_IsOnAmpRemoveFromAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        mic.remove_from_use()
        self.assertFalse(mic.is_on_amp())
    
    def test_IsOnAmpAmpToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        mic.place_on_amp()
        self.assertTrue(mic.is_on_amp())
        
    def test_IsInRoomNewToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
    
    def test_IsInRoomAmpToRoom(self):
        mic = Mic("SM57A")
        mic.place_on_amp()
        self.assertFalse(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
        
    def test_IsInRoomRoomToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
        mic.place_on_amp()
        self.assertFalse(mic.is_in_room())
        
    def test_IsInRoomRemoveFromRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
        mic.remove_from_use()
        self.assertFalse(mic.is_in_room())
    
    def test_IsInRoomRoomToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
        mic.place_in_room()
        self.assertTrue(mic.is_in_room())
    
    def test_HasBeenplacedNew(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
    
    def test_HasBeenplacedNewToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
    
    def test_HasBeenplacedNewToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
    
    def test_HasBeenplacedNewToRemoved(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.remove_from_use()
        self.assertFalse(mic.has_been_placed())
    
    def test_HasBeenplacedAmpToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
        
    def test_HasBeenplacedAmpToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
    
    def test_HasBeenplacedAmpToRemoved(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
        mic.remove_from_use()
        self.assertFalse(mic.has_been_placed())
    
    def test_HasBeenplacedRoomToAmp(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
        mic.place_on_amp()
        self.assertTrue(mic.has_been_placed())
    
    def test_HasBeenplacedRoomToRoom(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
    
    def test_HasBeenplacedRoomToRemoved(self):
        mic = Mic("SM57A")
        self.assertFalse(mic.has_been_placed())
        mic.place_in_room()
        self.assertTrue(mic.has_been_placed())
        mic.remove_from_use()
        self.assertFalse(mic.has_been_placed())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()