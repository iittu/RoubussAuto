#based on python3.5.3 or later
#Author: EHYNAII

import sys
sys.path.append('../')
from config import GetSetup
#from GetSetup import ConfigDict
from time import sleep

from pexpect import pxssh

import _thread

hostname = GetSetup.ConfigDict['board_ip']
username = GetSetup.ConfigDict['board_username']
password = GetSetup.ConfigDict['board_password']
logpath  = GetSetup.ConfigDict['log_path']
scrptpath= GetSetup.ConfigDict['script_path']
failstr  = GetSetup.ConfigDict['failure_check_str']

ssh = pxssh.pxssh()

def BoardLogin():
    return ssh.login(hostname, username, password, 22)

def TestRun():
    global scrptpath
    global logpath
    return ssh.sendline('sh ' + scrptpath + ' > ' + logpath + ' &')

def RaiseFailureCheckThread():    
    global logpath
    global failstr
    ssh.sendline('echo "echo "" > ' + logpath + '.fail" > ' + logpath + '.chk.sh')
    ssh.sendline('echo "while [ 1 -eq 1 ]" >> ' + logpath + '.chk.sh')
    ssh.sendline('echo "do" >> ' + logpath + '.chk.sh')
    ssh.sendline('echo "cat ' + logpath + ' | grep ' +  failstr + ' >> ' + logpath + '.fail" >> ' + logpath + '.chk.sh')
    ssh.sendline('echo "sleep 0.8" >> ' + logpath + '.chk.sh')
    ssh.sendline('echo "done" >>' + logpath + '.chk.sh')
    ssh.sendline('sh ' + logpath + '.chk.sh &')

def LogMonitor(delay=1):
    global logpath
    while 1:
        ssh.sendline('tail -n 5 ' + logpath)
        ssh.prompt()
        print(ssh.before.decode())
        sleep(delay)

def FailureCheck(delay=5):
    global logpath
    while 1:
        ssh.sendline('cat ' + logpath + '.fail')
        ssh.prompt()
        print(ssh.before.decode())
        sleep(delay)

print(BoardLogin())
print(TestRun())
RaiseFailureCheckThread()

try:
   _thread.start_new_thread( LogMonitor, (1,) )
   _thread.start_new_thread( FailureCheck, (5,) )
except:
   print ("Error: Could not start Thread")

while 1:
   pass


