import socket
sock = socket.socket()
a0=int(input("Enter Port:"))
result = sock.connect_ex(('127.0.0.1',a0))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
