import bluetooth
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("E0:63:E5:29:49:91",15))
sock.send("asdasdas")
print "end"