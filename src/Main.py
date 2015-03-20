'''
Created on Mar 20, 2015

@author: desposito
'''
from Amplifier import Amplifier
from Instruments.GibsonSG import GibsonSG
from Interfaces.Focusrite_Saffire_Pro40 import Focusrite_Saffire_Pro40
from Interfaces.IMP2 import IMP2
from Mics.SM57 import SM57
from Mics.MK319 import MK319
from Pedals.Compressor import Compressor
from Pedals.Gate import Gate

def Main():
    Guitar = GibsonSG()
    Comp = Compressor(threshold=4, tone=5, level=10, connected_device=Guitar)
    NoiseGate = Gate(threshold=4, connected_device=Comp)
    DI_Box = IMP2(connected_device=NoiseGate)
    Amp = Amplifier(connected_device=DI_Box)
    Amp.Set_Clean_Channel(4, 8, 3, 8)
    Amp.Set_Drive_Channel(7, 7, 3, 7, 5, 4)
    Amp.Set_Master_Channel(4)
    SM57A = SM57("SM57A")
    SM57A.Place_On_Amp(9, 3, 0, 0, 1)
    MK319A = MK319("MK319A")
    MK319A.Place_On_Amp(0, 0, 0, 0, 1)
    IFace = Focusrite_Saffire_Pro40(5)
    IFace.AnalogInputs[1].ConnectedDevice = DI_Box
    IFace.AnalogInputs[2].ConnectedDevice = SM57A
    IFace.AnalogInputs[4].ConnectedDevice = MK319A
    IFace.PhantomPower[1].Turn_On()

if __name__ == '__main__':
    Main()