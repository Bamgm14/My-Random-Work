import socket
s=socket.socket()
def a(s,n):
    s.connect(('202.88.238.3',n))
    sock.bind(('',A))
    print ('Phase1')
    sock.listen(10)
    c,a=s.accept()
    print(c)
for x in range(100000):
    try:
        a(s,x)
        print (x,'Success')
    except:
        print (x,'Fail')
        continue
