import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
ser = serial.Serial(port = '/dev/ttyUSB0')
if ser.isOpen() == False:
	ser.open()

ser.write('>03050000 39 00[CR]')
time.sleep(1)
out = ''
while True:
	out += ser.read(1)
	if out != '':
		print '>> ' + out