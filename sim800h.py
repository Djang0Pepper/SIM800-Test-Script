#!/usr/bin/python2
'''
Project	 	: Offone
Date&Time	: 19th Jun 2018.
Description	: This is test script for SIMcom SIM800H module
		http://simcomm2m.com/En/module/detail.aspx?id=75
'''
import time, sys
from sim800h_api import SIM800H


COMPORT_NAME 	= "/dev/ttyUSB0"
VERSION		= "0.0.2"

def main():
	sim800h = SIM800H(portName=COMPORT_NAME)
	sim800h.openComPort()

	print("..######..####.##.....##..#######....#####.....#####...##.....##\
\n\r.##....##..##..###...###.##.....##..##...##...##...##..##.....##\
\n\r.##........##..####.####.##.....##.##.....##.##.....##.##.....##\
\n\r..######...##..##.###.##..#######..##.....##.##.....##.#########\
\n\r.......##..##..##.....##.##.....##.##.....##.##.....##.##.....##\
\n\r.##....##..##..##.....##.##.....##..##...##...##...##..##.....##\
\n\r..######..####.##.....##..#######....#####.....#####...##.....##\
" + "\n\r\t Test module written for SIMcom SIM800H module \n\r\t\t\t   v" + VERSION)	

	if not sim800h.checkCommunication():
		print("[FAILED] - couldn't communicate with module")
		sys.exit()

	while 1:
		print '\n\r-----------------'
		print 'Choose operation:'
		print '1 - Send SMS'
		print '2 - Call'
		print 'q - Quit program'
		print '-----------------'
		try:
		    in_selection = ''
		    in_selection = raw_input('>> ')
		except Exception, e:
		    logging_device.debug('Error: ' + str(e))
		    break
		else:
		    if in_selection == '1':
			if not sim800h.sendSms():
				print("[FAILED] - Send SMS")
			print("SMS sent successfully")

		    elif in_selection == '2':	                
			if not sim800h.call():
				print("[FAILED] - to Make a call")
			print("Successfully ended call")

		    elif in_selection == 'q':
			sim800h.openComPort()
			print("Thank you for using SIM800H app")
			time.sleep(0.3)
			sys.exit()
		    else:
			print("Wrong selection.\n")


if __name__ == "__main__":
	main()
	print("End of module")
#EOF
