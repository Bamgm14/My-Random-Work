import time
a=input("Input Number Of Servers:")
q=time.time()
f=open("Server.py","w+")
f.write("import socket\nimport threading\n")
f.write("\ndef t():\n\twhile True:\n\t\tx = input('Enter input:\\n')\n\t\tsock = socket.socket()\n\t\tsock.connect(('127.0.0.1',a0))\n\t\tsock.send(x.encode('utf-8'))\n\t\tsock.close()\n")
def b(n):
    if n.isalpha():
        print ("Invalid Input")
        time.sleep(5)
        exit()
    else:
        a=int(n)
        b=ord('A')
        for x in range(a):
            f.write(chr(b+x)+"=int(input('Enter Other Port "+str(x+1)+":'))\ndef t"+str(x)+"():\n\tsock = socket.socket()\n\tsock.bind(('',"+chr(b+x)+"))\n\tsock.listen(10)\n\twhile True:\n\t\tc, addr = sock.accept()\n\t\tprint('User"+str(x+1)+":',c.recv(1024).decode('utf-8'))\n\t\tc.close()\n")
    return n
b(a)
f.write("sock = socket.socket()\na1=input('Do You Want To Search For Port (Y/N):')\nif a1=='y' or a1=='Y':\n\tprint ('Active Servers:\\n')\n\tfor x in range(A,A+1+"+a+"):\n\t\tresult= sock.connect_ex(('127.0.0.1',x))\n\t\tif result == 0:\n\t\t\tprint (x,'\\n')\n\t\telse:\n\t\t\tcontinue\n")
f.write("a0=int(input('Your Port:'))\n")
for x in range(int(a)):
    f.write("thread"+str(x)+" = threading.Thread(target=t"+str(x)+",args=())\n")
f.write("thread = threading.Thread(target=t,args=())\nthread.start()\n")
for x in range(int(a)):
    f.write("thread"+str(x)+".start()\n")
f.close()
w=time.time()
print ("Server Created In",w-q)
