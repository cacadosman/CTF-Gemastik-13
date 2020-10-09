#!/usr/bin/env python3

from Crypto.Util.number import *
import random
from os import urandom
import time
import sys

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def genKey():
	p = getPrime(1337)
	q = getPrime(1337)
	e = 0x10001
	n = p*q
	phi = (p-1)*(q-1)
	d = inverse(e,phi)
	x = (random.randint(-9,9)*p + q)*(random.randint(-9,9)*q + p)
	y = (p + random.randint(-9,9)*q)*(q + random.randint(-9,9)*p)
	return n,e,d,x,y


def getVerySecureSeed(init):
	value     =  bytes_to_long(init)
	ret_seed  =  len(init)
	ret_seed ^=  ((value >> 437) & 28391)
	ret_seed |=  ((value >> 488) & 1273) 
	ret_seed -=  ((value >> 432) ^ 734)
	ret_seed |=  ((value >> 484) & 9102)
	ret_seed +=  ((value >> 443) | 8764)
	ret_seed |=  ((value >> 528) & 9283)
	ret_seed -=  ((value >> 506) + 89827)
	ret_seed +=  ((value >> 433) - 9234)
	ret_seed ^=  ((value >> 494) % 23452)
	ret_seed -=  ((value >> 445) | 12)
	ret_seed ^=  ((value >> 438) * 928)
	ret_seed -=  ((value >> 477) ^ 8542)
	ret_seed +=  ((value >> 444) << 176)
	ret_seed |=  ((value >> 521) * 3)
	ret_seed ^=  ((value >> 513) + 999)
	return ret_seed

flag = open("flag.txt").read()
seed = getVerySecureSeed(flag.encode())
random.seed(seed)
target = 9

for i in range(10):
	n,e,d,x,y = genKey()

	plain = bytes_to_long(urandom(21))
	enc_plain = pow(plain, e, n)
	dec_plain = pow(enc_plain, d, n)
	
	print("Solve 10 stage to get the flag")
	print("n = {}".format(n))
	print("e = {}".format(e))
	print("c = {}".format(enc_plain))
	print("x = {}".format(x))
	print("y = {}".format(y))
	input_dec = input("Give me decrypted c : ")
	
	try:
		start = time.time()
		input_dec = int(input_dec)
		end = time.time()
		if end - start > 5:
			print("Times Up")
			break
		if input_dec == dec_plain:
			print("Nice")
		else:
			print("Not Nice")
			break
		if i == target:
			print("Congrats")
			print(flag)
	except:
		print("Something Error")
		break
