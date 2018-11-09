#/lib/x86_64-linux-gnu/libc.so.6
#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pwn import *
import base64
import libnum
from Crypto.Cipher import AES


io = remote("arcade.fluxfingers.net",1821)

def xor(info):
	io.recvuntil("-----------------------------*\n")
	io.sendline("XOR")
	io.recvuntil("Please choose the operand in hex >>> ")
	io.sendline(hex(info))
	io.recvuntil("Ciphertext is  ")
	return io.recvuntil("\n\n------------------------------",drop=True)

def add(info):
	io.recvuntil("-----------------------------*\n")
	io.sendline("ADD")
	io.recvuntil("Please choose the operand in hex >>> ")
	io.sendline(hex(info))
	io.recvuntil("Ciphertext is  ")
	return io.recvuntil("\n\n------------------------------",drop=True)

def dec(key):
	info = base64.b64encode(key)
	io.recvuntil("-----------------------------*\n")
	io.sendline("DEC")
	io.recvuntil("Enter the key base64 encoded >>> ")
	io.sendline(info)
	io.recvuntil("Decryption is  ")
	return io.recvuntil("\n------------------------------",drop=True)

def oracle():
	bit_length = 32*8
	known = ""
	for i in range(bit_length):
		info = int("1".ljust(i+1,"0"),2)
		print "info:",info,len(bin(info)[2:].strip("L"))
		xor_res = xor(info)
		add_res = add(info)
		print len(xor_res),len(add_res)
		if xor_res == add_res:
			known = "0" + known
		else:
			known = "1" + known
		print "known:",known,len(known)
	key = libnum.n2s(int(known,2))
	print dec(key)
	key = libnum.n2s(int(known[-128:],2))
	print dec(key)
	key = libnum.n2s(int(known[-192:],2))
	print dec(key)
	key = libnum.n2s(int(known,2))
	cryptor = AES.new(key, AES.MODE_ECB)
	print cryptor.decrypt(base64.b64decode(xor(0)))

oracle()
io.interactive()