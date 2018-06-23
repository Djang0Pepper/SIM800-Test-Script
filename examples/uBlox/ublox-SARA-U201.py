import serial
import time

SERVER 	= "api-demo.wolkabout.com"
PORT 	= 1883 

class UbloxSaraU201:
	def __init__(self, destination="api-demo.wolkabout.com", port=1883, command=""):
		self.destination = destination
		self.port = port
		self.command = command

	def openComPort(self):
		self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
		time.sleep(1)

	def closeComPort(self):
		self.ser.close()

	def sendAtCommand(self, command):
		self.command = command
	
		self.ser.write(command + '\r')
		received=self.ser.read(150)
		print(received)
		#time.sleep(1)


print("************************** START **************************")

list_of_commands = ["AT+COPS?", "AT+CGDCONT=1,\"IP\",\"m2m.tele2.com\"", "AT+CGEQREQ=1,3,64,64,,,0,320,\"1E4\",\"1E5\",1,,3", "AT+UPSND=1,8", "AT+UPSD=1,1,\"m2m.tele2.com\"", "AT+UPSD=1,2,\"vipmobile\"", "AT+UPSD=1,3,\"vipmobile\"", "AT+UPSD=1,7,\"0.0.0.0\"", "AT+UPSDA=1,1", "AT+UPSDA=1,3", "AT+UIPCONF=?", "AT+UPING=\"api-demo.wolkabout.com\""]

connect = UbloxSaraU201(SERVER, PORT)
connect.openComPort()

for i in range(len(list_of_commands)):
	print(list_of_commands[i])
	
	connect.sendAtCommand(list_of_commands[i])

#add ping

print("************************** END **************************")
connect.closeComPort()
