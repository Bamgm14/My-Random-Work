p=7572438955050902848921685822765976161831338581004101731125915847287800060361248884557653227181713406954725866898588928615599735121978784650029075946468649
q=8344115849660956866866215095130574599471671151193655160185223959260078322957406054594462686291299877310582767933711148309248130971193227495016902919542469
e=65537
n=p*q
phin=(p-1)*(q-1)
def inverse(u, v):

    u3, v3 = int(u), int(v)
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1*q
        u3, v3 = v3, u3 - v3*q
    while u1<0:
        u1 = u1 + v
    return u1   
d=inverse(e,phin)
import struct
import sys
def long_to_bytes(n, blocksize=0):
    
    s = b''
    n = int(n)
    pack = struct.pack
    while n > 0:
        s = pack('>I', n & 0xffffffff) + s
        n = n >> 32
    
    for i in range(len(s)):
        if s[i] != b'\x00'[0]:
            break
    else:
        s = b'\x00'
        i = 0
    s = s[i:]
    if blocksize > 0 and len(s) % blocksize:
        s = (blocksize - len(s) % blocksize) * b'\x00' + s
    return s

def bytes_to_long(s):
    acc = 0

    unpack = struct.unpack

    if sys.version_info[0:3] < (2, 7, 4):
        if isinstance(s, bytearray):
            s = bytes(s)
        elif isinstance(s, _memoryview):
            s = s.tobytes()

    length = len(s)
    if length % 4:
        extra = (4 - length % 4)
        s = b'\x00' * extra + s
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', s[i:i+4])[0]
    return acc
a=input("Enter Code:")
a=a.encode()
a=bytes_to_long(a)
b=pow(a, e, n)
print (long_to_bytes(b))
