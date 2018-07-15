f = open("encryption.encrypted.py","r")
f2 = open("encryption.py","w")
info = f.read()
enc = "abcdefghijklmnopqrstuvwxyz"
#adg -> def
#gqhb -> from
#pbkhqw -> import
#qdwzqe -> return
#kqpew -> print
#urtd64 -> base64
enc = "abcdefghijklmnopqrstuvwxyz"
dec = "dm enwfoxgpyh  ira sbktclu" 

enc_list = []
for x in enc:
	enc_list.append(x)
dec_list = []
for x in dec:
	dec_list.append(x)

res = ""
for x in info:
	if ord(x)<=("z") and ord(x)>=ord("a"):
		index = ord(x)-ord("a")
		res += dec_list[index]
	else:
		res += x
print res
f2.write(res)