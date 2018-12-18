#!/usr/bin/python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import *


def menu():
    print()
    print('[1] Encrypt')
    print('[2] Decrypt')
    print('[3] Exit')
    return input()


def encrypt(m):
    return pow(m, rsa.e, rsa.n)


def decrypt(c):
    return pow(c, rsa.d, rsa.n)


rsa = RSA.generate(1024)
print rsa.e
