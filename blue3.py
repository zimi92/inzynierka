import bluetooth
import threading
import socket
import serial
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)	
sock.bind(("",14))
port = sock.getsockname()[1]
sock.listen(1)
data = ""
data1 = ""
cl_sock, cl_inf = sock.accept()
class receiverBT(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			global data 
			while data != "close":
				
				data=cl_sock.recv(1024)
				print data
			print "koniec "
		except(IOError):
			print "recvc not work"
		print "endRecvBt"
	
class senderBt(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			print "trying to establishe connectiion"
			sock.connect(("E0:63:E5:29:49:91",14))
			print "success"
			while True:
				data1=raw_input()
				if len(data1) == 0:
					break
				sock.send(data1)
				print data1
			print "koniec "
		except(IOError):
			print "send func not work"
		print "endSendBT"
class senderSer(threading.Thread):
        def __init__(self):
                threading.Thread.__init__(self)
                self.dataLocal = ""
                try:
                        if(False):
                                ports = list(serial.tool.list_ports.comports())
                                ser = serial.Serial(port = '/dev/ttyUSB0')
                                if ser.isOpen() == False:
                                        ser.open()
                
                except(IOError):
                        print "Serial sender doesn't work"
        def run(self):
                global data
                dataLocal = ""
                while( True):
                        if data != dataLocal:
                                print data
                        dataLocal = data                       
recivBt = receiverBT()
recivBt.start()
sendBt = senderBt()
sendBt.start()
sendSer = senderSer()
sendSer.start()
