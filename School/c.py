from Crypto.Util.number import *
x=1
c=[]
d=1791401263369046055405501295526897108530470568468061619495765286198094480354281525615870609621314792068208337946818441118405155370358661832301519554660011
a=78448823099576055514414361317662315054325962383563105820765456804663944126101480094518811906000472963835962831013758061692111051241607550849092731437379369044347640203022241971010262069670465388627263720813285059155866651504979066160700686173441572263502395651150476843944960357736597981882527397598286672207
while True:
    b=getPrime(512)
    print (b)
    if b not in c:
        if (d-b)*b==a:
            print (b)
            c.append(b)
            break
        else:
            print (x)
            x+=1
            c.append(b)
            continue
    else:
        print (c)