# -*- coding: utf-8 -*-  
import libnum
import base64
from Crypto.Cipher import AES
def num2str(num):
    h=hex(num)[2:].replace("L","")
    if len(h)%2 ==0 :
        return h.decode("hex")
    else:
        return ("0"+h).decode("hex")
def str2num(str):
    return int(str.encode("hex"),16)
def aes_cbc_decode(password,iv,c):
    cipher = AES.new(password, AES.MODE_CBC, iv)
    return cipher.decrypt(c)

n=0x595213e8b5e2e249bb3875b51de7c6d28d3dccc0a176c3cf6f3e3d3caed0c3050d9cf6e9b61245aefbea04fdcbac2e4e4495366042f490a6de7a3a736b56afd3284279ff2a972481419c3fce40116d19090b1db4829fac3e124bb8527f07e770ba9f5514a9ffe468db182de7f68331f462d2adaf34534df2c1633a267bd9a2b3da6777ea95d724efd475643da40b2515f9130abda8b633aa9317d64e61c82d7b6f338e09c29797b07ce6eccffbc63ecb81231982e745233df2334c115cbb054ef82483bbb223cf2e62a26f12b2f64aa666c8d1ad2a274590225d4940243c0909bbe1bcd8a99c8f9fb53e3f83a4ecb40effa7277d334fac6266e3187e8a0a2117
e=0x10001
cflag = "HTDpx+5Tfy3CcgvirHME+2ztubm9avySIT6SVxPbklo="
info = "#0x4633c8ecff00f49d9510aa752d948937cd470080d8553026dc9cb115e1f16fdb4c88d047e80d748aff8ae5c5017ec375ec85106b9dac4ffc7a2691ba661bf6c4d49029ade468cb05c83fbeebc855e210abd6595e46496078c7041dae7a779bcc4e34a4b7762debb4e7ea3315f91ad7693c3c197d2bb7969780624c5e073fffdc8e0b3094502acdb37ccc8ec2f90156236ee28ae1875ec58c14d4750f69d8b83ce7438a2454d7cad7d303dc2be19781b0042f1a721a65212c86dbeeb69283b1e34933d46e1f87f44f91a484ba731a621af5ed2865716d78f366775f3e76172986ab617506e03b96bdccc59eaa300130e738626708dfc732068f0574350abedf2f#0x121973bfd8abf561158b63dfe57d7b3616d71eac3959ef15fa7a25998ef8e487252fcf45c8feeabb35fa130aa63bbaba7b6136fd386a968612656cc6880bdf7e5fcd9b5d6b8f386858c440302ac3de3052eada6cc3b8f24d62dc809c0507d960a8f8da86630a4056e43afa90b01969c9e7de73a5bc384eb5d9fecc3fd00a0154d30ab71f5314e284d3a51c69519d8bac42e6f85cf5b585c302e35e652742706fb4c418fc978bf7fdbc92a19d029b0a025eef07ce73f2ba50339ae1a5088e604279bcc32aa8cd8dbc7a10f7b68b04c41f2668d21b494aeb8d81ec757882c8c8ffb00e5e1f7f55f612c49f37961c39d77b764d6216899232fd3d00f4dda2f067ef#c8e15e451066c74d2e412ab6aafc03125747e94c8fae6f5b2dcb4569f3b0ca81a02c5766d3aa99cda2d311157c68d493ad372071121a5dc1eb3bb58eb00cbaf9add9b1c4ebfa392712c07c977df1ebd61e7f14d8c1d3ba5db219##"
info = info.split("#")
ck = int(info[1],16)
civ = int(info[2],16)
p_high = int(info[3],16)
print ck,civ,hex(p_high)
print len(bin(p_high).strip("0b").strip("L"))
print 1024 - len(bin(p_high).strip("0b").strip("L"))
x = 0x4e739db6fe4c2881897874d4c24f98778d3dda2dff259242770290f2b19d2e92a67794b9c9b1
p = p_high<<304
p = p + x
q = n/p
phi_n = (p-1)*(q-1)
d = libnum.invmod(e,phi_n)
k = pow(ck,d,n)
iv = num2str(pow(civ,d,n))
aes_key = num2str(k)
print aes_key,iv
f = base64.b64decode(cflag)
print aes_cbc_decode(aes_key,iv,f)
