from Crypto.Util.number import *
from Crypto.PublicKey import RSA



#p = getPrime(1024)
#q = gmpy2.next_prime(13 * p)

print(p)
n = p*q
e = 65537
#13*(p**2)
calc = n - 5
#p**2
calc = calc // 13

#insert algorithm to calculate sqrt of humongous numbers
p
q = gmpy2.next_prime(13*p)

d = inverse(e,tot)
print(long_to_bytes(c,d,n)

"""
pubkey = "e: " + str(e) + "\n" + "n: " + str(n)
phin = (p-1)*(q-1)

assert GCD(e, phin) == 1

m = bytes_to_long(flag)

ciphertext = pow(m, e, n)
ciphertext = long_to_bytes(ciphertext)

obj1 = open("ciphertext.txt",'w')
obj1.write(ciphertext.encode("hex"))

obj2 = open('publickey.txt','w')
obj2.write(pubkey)
"""
