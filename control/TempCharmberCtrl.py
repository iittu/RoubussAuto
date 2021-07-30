#based on python3.5.3 or later
#Author: EHYNAII


import pysnooper
import sys
sys.path.append('../')
from control import SerialTrx
from time import sleep


#@pysnooper.snoop(depth=4)
def TempStatus(Charmber):
    SerialTrx.SerialSendStr(Charmber,"$01I")

#@pysnooper.snoop()
def TempSet(Charmber,Temp):
    #SerialTrx.SerialWrt(Charmber,"$01I" + '\r\n')
    SerialTrx.SerialSendStr(Charmber,"$01E " + Temp + " 0000.0 0000.0 0000.0 010000000000")
    #SerialTrx.SerialWrt(Charmber,"$01I" + '\r\n')
    print('\r\n      TempSet sent!')
    TempStatus(Charmber)

#@pysnooper.snoop()
def TempChange(Charmber,StartTemp:int,StopTemp:int,SlewRate:int):
    TempInterval = abs(StopTemp - StartTemp)
    if StartTemp < StopTemp:
        TempAdd = 0
        while TempAdd <= TempInterval:
            TempSet(Charmber,str(StartTemp+TempAdd))
            TempAdd += SlewRate
            sleep(0.05966)
    else:
        TempAdd = 0
        while TempAdd <= TempInterval:
            TempSet(Charmber,str(StartTemp-TempAdd))
            TempAdd += SlewRate
            sleep(0.05966)

