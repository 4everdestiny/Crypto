import base64,libnum
info = open("ciphertext.txt","r").read()
print info,len(info)
info_b = base64.b64decode(info)
print len(info_b),hex(libnum.s2n(info_b))
print len(hex(libnum.s2n(info_b))[2:-1])
res = ""
for x in range(0,len(hex(libnum.s2n(info_b))[2:-1]),2):
	res += chr(255-int(hex(libnum.s2n(info_b))[2:-1][x:x+2],16))
print res