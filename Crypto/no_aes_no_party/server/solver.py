from pwn import *
from Crypto.Cipher import AES
import itertools

def dec_ecb(strs, key):
	obj = AES.new(key, AES.MODE_ECB)
	return obj.decrypt(strs)

HOST = "<insert targeted host here>"
PORT = 1234
r = remote(HOST, PORT)

r.sendlineafter("> ", "2")
flag_enc = r.recvline()[:-1].decode("hex")

r.sendlineafter("> ", "1")
key_enc = r.recvline()[:-1]

for i in range(255): # 8 byte plaintext dapet di iterasi ke 255
	print i
	r.sendlineafter("> ", "3")
	r.sendlineafter("Msg: ", key_enc)
	key_enc = r.recvline()[:-1]

real_key = key_enc.decode("hex")[:8]
liss = "".join(map(chr,range(256)))

for kars in itertools.product(liss, repeat=2):
	added = "".join(kars)
	final_key = real_key + (added*4)
	hasil = dec_ecb(flag_enc, final_key)
	if "gemastik13{" in hasil:
		print hasil
		break

