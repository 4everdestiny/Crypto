import zlib
import os

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.PublicKey import RSA
import libnum
from pwn import *
import base64

with open('pubkey.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
n = rsakey.n
e = rsakey.e
with open('key.enc') as f:
    key = f.read()
    enc_key = int(key)
#print enc_key
print libnum.nroot(27,3)
for i in range(1000000):
	temp = enc_key + i*n
	n_root = libnum.nroot(temp,e)
	if pow(n_root,e,n) == enc_key:
		print "find"
		print n_root
		res = n_root
		break
assert pow(res,e,n) == enc_key
key = libnum.n2s(res)
print key,len(key)
with open('file.enc') as f:
    file = f.read()
    enc_file = base64.b64decode(file)
print enc_file,len(enc_file)
res = ""
for i in range(len(key)):
	res += chr(ord(key[i])^ord(enc_file[i]))
print res