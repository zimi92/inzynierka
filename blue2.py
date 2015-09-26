import bluetooth
import thread
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)	
sock.bind(("",12))
port = sock.getsockname()[1]
sock.listen(1)
data = ""
cl_sock, cl_inf = sock.accept()
def bluetoothIn():
	try:
		data ="" 
		while data != "close":
			data=""
			data=cl_sock.recv(1024)
			print data
			print "koniec " + data
		print "koniec "
	except(IOError):
		print "func not work"
	print "end"
try:
	thread.start_new_thread(bluetoothIn, (),)
except:
	print "bluetoothIn doesn't start"