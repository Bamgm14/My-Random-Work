import socket
import threading

def t():
	while True:
		x = input('Enter input:\n')
		sock = socket.socket()
		sock.connect(('127.0.0.1',a0))
		sock.send(x.encode('utf-8'))
		sock.close()
A=int(input('Enter Other Port 1:'))
def t0():
	sock = socket.socket()
	sock.bind(('',A))
	sock.listen(10)
	while True:
		c, addr = sock.accept()
		print('User1:',c.recv(1024).decode('utf-8'))
		c.close()
sock = socket.socket()
a1=input('Do You Want To Search For Port (Y/N):')
if a1=='y' or a1=='Y':
	print ('Active Servers:\n')
	for x in range(A,A+1+1):
		result= sock.connect_ex(('127.0.0.1',x))
		if result == 0:
			print (x,'\n')
		else:
			continue
a0=int(input('Your Port:'))
thread0 = threading.Thread(target=t0,args=())
thread = threading.Thread(target=t,args=())
thread.start()
thread0.start()
