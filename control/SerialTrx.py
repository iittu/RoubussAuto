#based on python3.5.3 or later
#Author: EHYNAII


import pysnooper
import serial
import serial.tools.list_ports
from time import sleep
'''
import msvcrt
import array
'''


#@pysnooper.snoop()
def ListAvilablePorts():
    port_list = list(serial.tools.list_ports.comports())
    n = len(port_list)
    port_list_set = []

    if n <= 0:
        print ("The Serial port can't find!")
        print('')
    else:
        print('\r\n------Availible COM list:------')
        print('')
        s = 0
        f = 0
        while s < n:
             port_list[s] = list(port_list[s])
             #print (port_list[s][0])
             try:
                serialre = serial.Serial(port_list[s][0], 115200, timeout=0.5)  #/dev/ttyUSB0
                if serialre.isOpen() :
                    print(port_list[s][0],'Can be open')
                    serialre.close()
             except:
                pass
                print(port_list[s][0],'Can not be open, Please check ACCESS!')
                f +=1
             port_list_set.append(port_list[s][0])
             s = s + 1
        print('\r\n      Total',n,'port(s) can be found,' ,n-f,'port(s) can be used.')

#@pysnooper.snoop()
def SerialWrt(ComNo,Message):
    try:
        #print('\r\n      Transmitting the Message to',ComNo,'... \r\n')
        SerialOpt = serial.Serial(ComNo, 115200, timeout=1)
        SerialOpt.write(Message.encode())
        SerialOpt.flush()
        sleep(0.33)
        #SerialReadBack = SerialOpt.readline()                              #clear send read back line
        #print(SerialReadBack.decode())
        SerialReadBack = SerialOpt.read(SerialOpt.inWaiting())
        print(SerialReadBack.decode(), flush=True)
        SerialOpt.close()
    except:
        print('\r\n      Failed!')


def SerialSendStr(PortName,Message):
    ComNo = str(PortName)
    Message = str(Message) + '\r\n'
    SerialWrt(ComNo,Message)
