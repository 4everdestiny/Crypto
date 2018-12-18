from pwn import *
import libnum

def encrypt(m):
    p.sendlineafter("[3] Exit\n","1")
    p.sendlineafter("\nPlaintext > ",str(m))
    p.recvuntil("\nEncrypted: ")
    return int(p.recvuntil("\n",drop=True))

def decrypt(c):
    p.sendlineafter("[3] Exit\n","2")
    p.sendlineafter("\nCiphertext > ",str(c))
    info = p.recvuntil("\n",drop=True)
    if info == "Ho, ho, no...":
        return False
    else:
        p.recvuntil("Decrypted: ")
        return int(p.recvuntil("\n",drop=True))

def recvflag():
    p.recvuntil("Galf - ")
    return int(p.recvuntil("\n",drop=True),16)

context.log_level = "debug"
p = remote("199.247.6.180",16002)
c = recvflag()
e = 65537
e_2 = encrypt("\x02")
e_4 = encrypt("\x04")
e_8 = encrypt("\x08")
k1n = (2**e) - e_2
k2n = (4**e) - e_4
k3n = (8**e) - e_8
#print k1n,k2n
n = libnum.gcd(k1n,k2n,k3n)
log.success("n:"+str(n))
res = 1
for i in range(1):
    temp = pow(2,e,n)
    c = (c*libnum.invmod(temp,n))%n
    res *= 2
info = decrypt(c)
while not info:
    temp = pow(2,e,n)
    c = (c*libnum.invmod(temp,n))%n
    res *= 2
m = (info * (res))%n
print libnum.n2s(m)
    