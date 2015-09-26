import bluetooth
import threading
import socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)	
sock.bind(("",14))
port = sock.getsockname()[1]
sock.listen(1)
data = ""
cl_sock, cl_inf = sock.accept()
class receiverBT(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			data ="" 
			while data != "close":
				data=""
				data=cl_sock.recv(1024)
				print data
			print "koniec "
		except(IOError):
			print "recvc not work"
		print "end"
	
class senderBt(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		try:
			sock.connect(("E0:63:E5:29:49:91",15))
			while True:
				data=raw_input()
				if len(data) == 0:
					break
				sock.send(data)
				print data
			print "koniec "
		except(IOError):
			print "send func not work"
		print "end"
class sender():
        def __init__(self):
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.clientSocket = None
                self.clientAddress = None
                self.connected = False
                self.address = ''

recivBt = receiverBT()
recivBt.start()
sendBt = senderBt()
sendBt.start()
