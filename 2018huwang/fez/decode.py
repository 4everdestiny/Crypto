import libnum
def xor(a,b):
    assert len(a)==len(b)
    c=""
    for i in range(len(a)):
        c+=chr(ord(a[i])^ord(b[i]))
    return c

def map_test(info):
	return int(info,16)

def decrypt(test,test_K,flag_K):
	testL = libnum.n2s(test)[:27]
	testR = libnum.n2s(test)[27:54]
	test_KL = libnum.n2s(test_K)[:27]
	test_KR = libnum.n2s(test_K)[27:54]
	K1 = xor(testR,test_KL)
	K2 = xor(xor(test_KR,testL),testR)
	flag_KL = libnum.n2s(flag_K)[:27]
	flag_KR = libnum.n2s(flag_K)[27:54]
	flagR = xor(flag_KL,K1)
	flagLR = xor(flag_KR,K2)
	flag_L = xor(flagLR,flagR)
	print flag_L+flagR

f = open("fez.log","r")
info = f.read()[2:].replace("\x00","").split("\r\n")[:-1]
test,test_K,flag_K = map(map_test,info)
decrypt(test,test_K,flag_K)