#!/usr/bin/python2
'''
Project	 	: SIM800 test script 
Date&Time	: 08th August 2019.
Description	: This is test script for SIMcom SIM800H module
		http://simcomm2m.com/En/module/detail.aspx?id=75
'''
import time, sys
import logging
from sim800h_api import SIM800H


COMPORT_NAME 	= "/dev/ttyUSB0"
VERSION		= "0.0.3"

def main():
	print("..######..####.##.....##..#######....#####.....#####...##.....##\
\n\r.##....##..##..###...###.##.....##..##...##...##...##..##.....##\
\n\r.##........##..####.####.##.....##.##.....##.##.....##.##.....##\
\n\r..######...##..##.###.##..#######..##.....##.##.....##.#########\
\n\r.......##..##..##.....##.##.....##.##.....##.##.....##.##.....##\
\n\r.##....##..##..##.....##.##.....##..##...##...##...##..##.....##\
\n\r..######..####.##.....##..#######....#####.....#####...##.....##\
" + "\n\r\t Test module written for SIMcom SIM800H module \n\r\t\t\t   v" + VERSION)	

        logging.basicConfig(level=logging.DEBUG)

        sim800h = SIM800H(portName=COMPORT_NAME)
	sim800h.openComPort()


	if not sim800h.checkCommunication():
		logging.error("Couldn't communicate with module")
		sys.exit()

	while 1:
		print("\n\r-----------------\n\rChoose operation:\n\r1 - Send SMS\n\r2 - Call\n\rq - Quit program\n\r-----------------" )
		try:
		    in_selection = ''
		    in_selection = raw_input('>> ')
		except Exception as e:
		    logging.debug('Error: ' + str(e))
		    break
		else:
		    if in_selection == '1':
			    if sim800h.sendSms():
			        print("SMS sent successfully")
                            else:
			        logging.error("Send SMS")
		    elif in_selection == '2':	                
			    if sim800h.call():
	            	        print("Successfully ended call")
                            else:
				 logging.error("To Make a call")

		    elif in_selection == 'q':
			    sim800h.closeComPort()
			    print("Thank you for using SIM800H app")
			    time.sleep(0.3)
			    sys.exit()
		    else:
			    print("Wrong selection.\n")


if __name__ == "__main__":
	main()
	print("End of module")
#EOF
