import serial
import time

MINE = "+38164******8"

PHONE_NMBR = SOME_PHONE_NUMBER

class TextMessage:
	def __init__(self, recipient=PHONE_NMBR, message="TextMessage.content not set."):
		self.recipient = recipient
		self.content = message

	def setRecipient(self, number):
		self.recipient = number

	def setContent(self, message):
		self.content = message

	def connectPhone(self):
		self.ser = serial.Serial('COM47', 115200, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
		time.sleep(1)

	def sendMessage(self):
		self.ser.write('ATZ\r')
		time.sleep(1)
		self.ser.write('AT+CMGF=1\r')
		time.sleep(1)
		self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
		time.sleep(1)
		self.ser.write(self.content + "\r")
		time.sleep(1)
		self.ser.write(chr(26))
		time.sleep(1)

	def disconnectPhone(self):
		self.ser.close()

sms = TextMessage(PHONE_NMBR, "Hi, I sent this message from my computer")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print "message sent successfully"
