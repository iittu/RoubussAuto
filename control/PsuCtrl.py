# Haitian Yin
# This script is used for controlling the PSU remotely
# This should support all Lab instruments which supports LXI
# 2020-06-04 1st Ver.
# ver 0.1

import vxi11, sys, getopt
def main(argv):
	ipaddr = ''
	volt = ''
	curr = ''
	outp = ''
	
	try:
		opts, args = getopt.getopt(argv,"hi:v:c:o:",["ip=","voltage=","current=","output="])
	except getopt.GetoptError:
		print 'psu -i <ip address> -v [voltage value] -c [current value] -o [output:1/0]'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'psu -i <ip address> -v [voltage value] -c [current value] -o [output:1/0]'
			sys.exit()
		
		elif opt in ("-i", "--ip"):
			ipaddr = arg
		elif opt in ("-v", "--voltage"):
			volt = arg
		elif opt in ("-c", "--current"):
			curr = arg
		elif opt in ("-o", "--output"):
			outp = arg
			
	instr =  vxi11.Instrument(ipaddr)
	instr.write("Volt "+volt)
	instr.write("Curr "+curr)
	instr.write("OUTP "+outp)
	
	print "Output:  "+instr.ask("OUTP:STAT?")
	print "Voltage: "+instr.ask("Meas:Volt?")


if __name__ == "__main__":
	main(sys.argv[1:])

   