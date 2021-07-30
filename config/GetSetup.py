#based on python3.5.3 or later
#Author: EHYNAII

# capture the configuration Key Words for setup test environmnet


import sys
sys.path.append('../')
#import board

Fconfig = open('../board/setup.txt') # original file
ConstLine = Fconfig.readline()

ConfigDict={'product_name':'', 'board_ip':'', 'power_supplier_ip':'', 'board_com':'', 'charmber_com':'', 'script_path':'', 'log_path':'', 'high_temp':'', 'low_temp':'', 'slew_rate(degC/min)':'', 'start_temp':'', 'cycle_num':'', 'tester_mailbox':'', 'failure_check':'', 'report_path':'', 'failure_check_str':'', 'high_temp_dur':'', 'low_temp_dur':'', 'board_username':'root', 'board_password':'root'}

while ConstLine:
    #print(ConstLine.split(':')[0])
    if ConstLine.split(':')[0] in ConfigDict:
        ConfigDict[ConstLine.split(':')[0]] = ConstLine.split(':')[-1].strip('\n')
        #print(ConfigDict[ConstLine.split(':')[0]])
    ConstLine = Fconfig.readline()

Fconfig.close()

print(ConfigDict)
#print(ConfigDict['product_name'])
