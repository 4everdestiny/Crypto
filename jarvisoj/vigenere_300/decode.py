import libnum
from base64 import b64encode, b64decode
import binascii
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
chars2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
f = open("encrypted.txt","r")
info = f.read()
size_list = []

def shift(char, key, rev = False):
    if not char in chars:
        return char
    if rev:
        return chars[(chars.index(char) - chars.index(key)) % len(chars)]
    else:
        return chars[(chars.index(char) + chars.index(key)) % len(chars)]

def decrypt(encrypted, key):
    encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
    return b64decode(encrypted.encode('ascii')).decode('ascii')

def check(mes,key,i):
    #print mes,key,i
    if mes == "=" :
        return True
    index = (chars.index(mes) - chars.index(key)) % len(chars)
    index = chars2.index(chars[index])
    if i == 6:
        return index == chars2.index("l")
    if i == 7:
        return index == chars2.index("z")
    if i == 10:
        return index == chars2.index("E")
    if i == 11:
        return index == chars2.index("g")
    if i == 14:
        return index == chars2.index("F")
    if i == 15:
        return index == chars2.index("w")
    if i%4<=2:
        if index & 0b10 << ((2-i%4)*2) == 0:
            return True
        else:
            return False
    else:
        return True

def calcukeyrange(info,keylength):
    keyrange = [[]] * keylength
    assert len(keyrange) == keylength
    for i in range(keylength):
        temp_use = list(chars)
        for j in range(i,len(info)-1,keylength):
            temp_next = []
            for k in range(len(temp_use)):
                if check(info[j],temp_use[k],j):
                    temp_next.append(temp_use[k])
            temp_use = temp_next[:]
        keyrange[i] = temp_use[:]
    return keyrange
"""
for length in range(3,len(info)):
    for i in range(len(info)):
        for j in range(i+length,len(info)):
            if info[i:i+length] == info[j:j+length]:
                size_list.append(j-i)"""
key_length = 12
#368 = 4 * 2 * 2 * 23
#print decrypt(info,key)
length_max = 368/4*3
keyrange = calcukeyrange(info,key_length)
print keyrange
key = ""
for i in range(key_length):
    key += keyrange[i][0]
print b64encode("Jap")
print decrypt(info,key)