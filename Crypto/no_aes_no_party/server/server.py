#!/usr/bin/env python3

from Crypto.Cipher import AES
import binascii
import os
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


flag = open("flag.txt").read()
ulti_key = os.urandom(8)
adds_key = os.urandom(2)
main_key = os.urandom(16)
main_iv  = os.urandom(16)

def encrypt_1(strs, key, iv):
	obj = AES.new(key, AES.MODE_CFB, iv)
	return obj.encrypt(strs)

def encrypt_2(strs, key):
	obj = AES.new(key, AES.MODE_ECB)
	return obj.encrypt(strs)


while True:
	print("""We Open Encryption Service For Free\n1. Get Encrypted Key\n2. Get Encrypted Flag\n3. Encrypt Message""")
	option = input("> ")
	if option == "1":
		enc_ult_key = encrypt_1(ulti_key + os.urandom(24), main_key, main_iv)
		print(binascii.hexlify(enc_ult_key).decode())
	elif option == "2":
		enc_flag = encrypt_2(flag.encode(), ulti_key+(adds_key*4))
		print(binascii.hexlify(enc_flag).decode())
	elif option == "3":
		input_msg = input("Msg: ")
		try:
			input_msg = binascii.unhexlify(input_msg)
			enc_input_msg = encrypt_1(input_msg, main_key, main_iv)
			print(binascii.hexlify(enc_input_msg).decode())
		except:
			print("Invalid Msg")
	else:
		print("Invalid Option")
