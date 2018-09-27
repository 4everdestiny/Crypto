import libnum,base64

def test(s1,s2):
	res = ""
	for i in range(len(s1)):
		temp = ord(s1[i])^ord(base64.b64decode(s2)[i])
		res += chr(temp)
	return res

def kaisa(s,number):
	res = ""
	for i in range(len(s)):
		res += chr(ord(s[i])+number)
	return res

info1 = "GCc3HR0qJw89BiY4FxQXFjo7OkUxag=="
info1_1 = "QShiuOUjbgJOvmdINIO1YU"
info2 = "yhjHUIY4SRbjgyu8YF4AAF"
info22 = "MBw1PD0sK1EMMw4dBgAGZy00QTUpeQ=="
info3 = "WfJK4sGYWhba789bhVYWHA"
info33 = "HhIVP1wWNTwICQ4WVkFKPRwkLCMgfg=="
info4 = "It_there_always_truth?"
print test(info1_1,"GCc3HR0qJw89BiY4FxQXFjo7OkUxag==")
print test(info3,"GhsAPCcyLQEwPhUYFCYHNx0cHis3AA==")
print test(info2,"GhsAPCcyLQEwPhUYFCYHNx0cHis3AA==")
skr = test(info4,"GhsAPCcyLQEwPhUYFCYHNx0cHis3AA==")
print skr
print base64.b64decode("GhsAPCcyLQEwPhUYFCYHNx0cHis3AA==")

#GWHT{I'M_EV3ryWher2!!}