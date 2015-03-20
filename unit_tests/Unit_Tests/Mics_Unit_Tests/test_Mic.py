'''
Created on Mar 18, 2015

@author: desposito
'''
import unittest
from Mics.Mic import Mic

class Test(unittest.TestCase):

    def test_ValidateDefaultConstructor(self):
        M1 = Mic("SM57A")
        self.assertEqual(M1.Name, "SM57A")
        self.assertIn("SM57A", M1.names)
        self.assertIsNone(M1.Clock)
        self.assertIsNone(M1.Radius)
        self.assertIsNone(M1.XAngle)
        self.assertIsNone(M1.YAngle)
        self.assertIsNone(M1.Distance)
        self.assertIsNone(M1.Placed)
        
    def test_MultipleObjectsTrackSameListOfNames(self):
        M1 = Mic("SM57A")
        M2 = Mic("SM57B")
        self.assertEqual(M1.names, M2.names)
        
    def test_CannotUseDuplicateNames(self):
        M1 = Mic("SM57A")
        self.assertEqual(M1.Name, "SM57A")
        self.assertRaises(ValueError, Mic, "SM57A")

    def test_SetAttributeReturnsValueAfterPassingValidations(self):
        M1 = Mic("SM57A")
        value = M1._Set_Attribute(3.14, 0, 5)
        self.assertEqual(value, 3.14)
        
    def test_SetAttributePassesWhenSuppliedAnInteger(self):
        M1 = Mic("SM57A")
        value = M1._Set_Attribute(3, 0, 5)
        self.assertEqual(value, 3)
        
    def test_SetAttributeWithNonNumericRaisesException(self):
        M1 = Mic("SM57A")
        self.assertRaises(TypeError, M1._Set_Attribute, "dog", 0, 5)
        
    def test_SetAttributeWithLowLimitErrorRaisesException(self):
        M1 = Mic("SM57A")
        self.assertRaises(ValueError, M1._Set_Attribute, -2, 0, 5)
        
    def test_SetAttributeWithHighLimitErrorRaisesException(self):
        M1 = Mic("SM57A")
        self.assertRaises(ValueError, M1._Set_Attribute, 10, 0, 5)
        
    def test_SetAttributeAllowsNegativeNumbers(self):
        M1 = Mic("SM57A")
        value = M1._Set_Attribute(-5, -10, -1)
        self.assertEqual(value, -5)
        
    def test_SetClockUpdatesClockAttribute(self):
        M1 = Mic("SM57A")
        M1._Set_Clock(3)
        self.assertEqual(M1.Clock, 3)
    
    def test_MinimumClockIs1(self):
        M1 = Mic("SM57A")
        M1._Set_Clock(1)
        self.assertEqual(M1.Clock, 1)
        self.assertRaises(ValueError, M1._Set_Clock, 0)
        
    def test_MaximumClockIs12(self):
        M1 = Mic("SM57A")
        M1._Set_Clock(12)
        self.assertEqual(M1.Clock, 12)
        self.assertRaises(ValueError, M1._Set_Clock, 13)
        
    def test_SetRadiusUpdatesRadiusAttribute(self):
        M1 = Mic("SM57A")
        M1._Set_Radius(5)
        self.assertEqual(M1.Radius, 5)
    
    def test_MinimumRadiusIs0(self):
        M1 = Mic("SM57A")
        M1._Set_Radius(0)
        self.assertEqual(M1.Radius, 0)
        self.assertRaises(ValueError, M1._Set_Radius, -1)
        
    def test_MaximumRadiusIs15(self):
        M1 = Mic("SM57A")
        M1._Set_Radius(15)
        self.assertEqual(M1.Radius, 15)
        self.assertRaises(ValueError, M1._Set_Radius, 16)    
    
    def test_SetXAngleUpdatesXAngleAttribute(self):
        M1 = Mic("SM57A")
        M1._Set_XAngle(-80)
        self.assertEqual(M1.XAngle, -80)
        
    def test_MinimumXAngleIsMinus90(self):
        M1 = Mic("SM57A")
        M1._Set_XAngle(-90)
        self.assertEqual(M1.XAngle, -90)
        self.assertRaises(ValueError, M1._Set_XAngle, -91)
    
    def test_MaximumXAngleIs90(self):
        M1 = Mic("SM57A")
        M1._Set_XAngle(90)
        self.assertEqual(M1.XAngle, 90)
        self.assertRaises(ValueError, M1._Set_XAngle, 91)
        
    def test_SetYAngleUpdatesYAngleAttribute(self):
        M1 = Mic("SM57A")
        M1._Set_YAngle(89)
        self.assertEqual(M1.YAngle, 89)
        
    def test_MinimumYAngleIsMinus90(self):
        M1 = Mic("SM57A")
        M1._Set_YAngle(-90)
        self.assertEqual(M1.YAngle, -90)
        self.assertRaises(ValueError, M1._Set_YAngle, -91)
    
    def test_MaximumYAngleIs90(self):
        M1 = Mic("SM57A")
        M1._Set_YAngle(90)
        self.assertEqual(M1.YAngle, 90)
        self.assertRaises(ValueError, M1._Set_YAngle, 91)
        
    def test_SetDistanceUpdatesDistanceAttribute(self):
        M1 = Mic("SM57A")
        M1._Set_Distance(76)
        self.assertEqual(M1.Distance, 76)
        
    def test_MinimumDistanceIs0(self):
        M1 = Mic("SM57A")
        M1._Set_Distance(0)
        self.assertEqual(M1.Distance, 0)
        self.assertRaises(ValueError, M1._Set_Distance, -1)
    
    def test_MaximumDistanceIs120(self):
        M1 = Mic("SM57A")
        M1._Set_Distance(120)
        self.assertEqual(M1.Distance, 120)
        self.assertRaises(ValueError, M1._Set_Distance, 121)
    
    def test_PlaceOnAmpDefaultValues(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp()
        self.assertEqual(M1.Clock, 12)
        self.assertEqual(M1.Radius, 0)
        self.assertEqual(M1.XAngle, 0)
        self.assertEqual(M1.YAngle, 0)
        self.assertEqual(M1.Distance, 0)
        self.assertEqual(M1.Placed, "Amp")
        
    def test_PlaceOnAmpWithClock(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp(clock=6)
        self.assertEqual(M1.Clock, 6)
        
    def test_PlaceOnAmpWithRadius(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp(radius=6)
        self.assertEqual(M1.Radius, 6)
        
    def test_PlaceOnAmpWithXAngle(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp(x_angle=6)
        self.assertEqual(M1.XAngle, 6)
    
    def test_PlaceOnAmpWithYAngle(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp(y_angle=6)
        self.assertEqual(M1.YAngle, 6)
        
    def test_PlaceOnAmpWithDistance(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp(distance=6)
        self.assertEqual(M1.Distance, 6)
        
    def test_PlaceInRoomDefaultValues(self):
        M1 = Mic("SM57A")
        M1.Place_In_Room()
        self.assertIsNone(M1.Clock)
        self.assertIsNone(M1.Radius)
        self.assertIsNone(M1.XAngle)
        self.assertIsNone(M1.YAngle)
        self.assertEqual(M1.Distance, 60)
        self.assertEqual(M1.Placed, "Room")
        
    def test_PlaceInRoomWithDistance(self):
        M1 = Mic("SM57A")
        M1.Place_In_Room(36)
        self.assertEqual(M1.Distance, 36)
        
    def test_RemoveMicFromAmp(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp()
        self.assertEqual(M1.Placed, "Amp")
        M1.Remove_From_Use()
        self.assertIsNone(M1.Clock)
        self.assertIsNone(M1.Radius)
        self.assertIsNone(M1.XAngle)
        self.assertIsNone(M1.YAngle)
        self.assertIsNone(M1.Distance)
        self.assertIsNone(M1.Placed)
        
    def test_RemoveMicFromRoom(self):
        M1 = Mic("SM57A")
        M1.Place_In_Room()
        self.assertEqual(M1.Placed, "Room")
        M1.Remove_From_Use()
        self.assertIsNone(M1.Clock)
        self.assertIsNone(M1.Radius)
        self.assertIsNone(M1.XAngle)
        self.assertIsNone(M1.YAngle)
        self.assertIsNone(M1.Distance)
        self.assertIsNone(M1.Placed)
        
    def test_IsOnAmpNewToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        
    def test_IsOnAmpRoomToAmp(self):
        M1 = Mic("SM57A")
        M1.Place_In_Room()
        self.assertFalse(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        
    def test_IsOnAmpAmpToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        M1.Place_In_Room()
        self.assertFalse(M1.Is_On_Amp())
        
    def test_IsOnAmpRemoveFromAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        M1.Remove_From_Use()
        self.assertFalse(M1.Is_On_Amp())
    
    def test_IsOnAmpAmpToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        M1.Place_On_Amp()
        self.assertTrue(M1.Is_On_Amp())
        
    def test_IsInRoomNewToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
    
    def test_IsInRoomAmpToRoom(self):
        M1 = Mic("SM57A")
        M1.Place_On_Amp()
        self.assertFalse(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
        
    def test_IsInRoomRoomToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
        M1.Place_On_Amp()
        self.assertFalse(M1.Is_In_Room())
        
    def test_IsInRoomRemoveFromRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
        M1.Remove_From_Use()
        self.assertFalse(M1.Is_In_Room())
    
    def test_IsInRoomRoomToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
        M1.Place_In_Room()
        self.assertTrue(M1.Is_In_Room())
    
    def test_HasBeenPlacedNew(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedNewToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedNewToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedNewToRemoved(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Remove_From_Use()
        self.assertFalse(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedAmpToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
        
    def test_HasBeenPlacedAmpToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedAmpToRemoved(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Remove_From_Use()
        self.assertFalse(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedRoomToAmp(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Place_On_Amp()
        self.assertTrue(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedRoomToRoom(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
    
    def test_HasBeenPlacedRoomToRemoved(self):
        M1 = Mic("SM57A")
        self.assertFalse(M1.Has_Been_Placed())
        M1.Place_In_Room()
        self.assertTrue(M1.Has_Been_Placed())
        M1.Remove_From_Use()
        self.assertFalse(M1.Has_Been_Placed())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValidateDefaultConstructor']
    unittest.main()