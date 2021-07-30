#based on python3.5.3 or later
#Author: EHYNAII


import sys
sys.path.append('.')
from control import SerialTrx
from control import TempCharmberCtrl
from common import Intro

#pysnooper.snoop(depth=2)
Intro.IntroPrint()


if __name__ == '__main__':
    #for CheckCom in port_list_set:
    SerialTrx.ListAvilablePorts()
    print('')

try:
    SerialTrx.SerialSendStr('COM24','transmit command \r\nread back line 1 ...\r\nread back line 2 ... ...')        #CTRL-C \x03
    TempCharmberCtrl.TempSet('COM24', '55')
    TempCharmberCtrl.TempChange('COM24',110,105,1)
except:
    print('\r\n      Error when transmitting!\r\n')


