import libnum
def dec(enc,key):
	res = ""
	for i in range(len(enc)):
		res += chr(ord(enc[i])^ord(key[i%len(key)]))
	return res
info = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
#ctflearn{
sp = info.split(",")
enc = info
key = "jowls"
print enc,key
print dec(enc,key)
print hex(ord("\t")^ord("c"))
print chr(ord("\t")^ord("c"))