import socket
sock = socket.socket()
print ("Available Server:\n")
for x in range(1000,1501):
    result= sock.connect_ex(('127.0.0.1',x))
    if result == 0:
        print (x,'\n')
    else:
        continue
