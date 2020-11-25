import socket
sock = socket.socket()
a=int(input("Enter Number:"))
result = sock.connect_ex(('127.0.0.1',a))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
