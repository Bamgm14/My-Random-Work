from Crypto.Cipher import AES


def padding(message, block_size):    
	ch = block_size - len(message) % block_size
	return message + bytes(chr(ch) * ch)


def AES_encrypt(key, message):
	a = AES.new(key,AES.MODE_ECB)
	ciphertext = a.encrypt(padding(message,16))
	return ciphertext 


if __name__=="__main__":
	key = "fq3tjj#fm3)49faf"
	cip = AES_encrypt(key,'')
	f = open('a.txt','wb')
	f.write(cip.encode('hex'))
	f.close()
	print AES.MODE_ECB
