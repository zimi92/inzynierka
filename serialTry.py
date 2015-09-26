import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
sed = serial.Serial(0)
if ser.isOpen() == False:
	ser.open()

ser.write('>03050000 39 00[CR]')
time.sleep(1)
while ser.inWaiting() > 0:
	out += ser.read(1)
	if out != '':
		print '>> ' + out