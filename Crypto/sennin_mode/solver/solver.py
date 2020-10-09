from sage.all import *
from pwn import *
from Crypto.Util.number import *
from multiprocessing import Process, Manager
from sympy import isprime


manager = Manager()
HOST = "<insert targeted host here>"
PORT = 1234

def solve_equation(eq1_value, eq2_value, params, ret):
	ret["result"] = None
	p_, q_ = var("p_ q_")
	eq1 = (params[0]*p_ + q_)*(params[1]*q_ + p_) == eq1_value
	eq2 = (p_ + params[2]*q_)*(q_ + params[3]*p_) == eq2_value
	ret["result"] = solve([eq1, eq2], p_, q_)
	print("solvable")
	

def find_seed():
	for kar in range(97,96,-1):
		init = b"gemastik13{" + chr(kar).encode() + b"A"*53 + b"}"
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

		r = remote(HOST, PORT)
		print("brute:",chr(kar))

		random.seed(ret_seed)
		print(r.recvline())
		n_recv = int(r.recvline().decode()[:-1].split("n = ")[1])
		r.recvline()
		r.recvline()
		x_recv = int(r.recvline().decode()[:-1].split("x = ")[1])
		y_recv = int(r.recvline().decode()[:-1].split("y = ")[1])
		r.close()
		param_input = [random.randint(-9,9) for i in range(4)]

		return_dict = manager.dict()

		proc = Process(target=solve_equation, args=(x_recv, y_recv, param_input, return_dict))
		proc.start()
		proc.join(timeout=4)
		proc.terminate()
		if return_dict["result"]:
			for obj in return_dict["result"]:
				try:
					p_temp = int(obj[0].rhs())
					q_temp = int(obj[1].rhs())
				except:
					continue
				if p_temp*q_temp == n_recv:
					print("Dapet Seed")
					return ret_seed



seed = find_seed()

r = remote(HOST, PORT)

random.seed(seed)
for i in range(10):
	param_input = [random.randint(-9,9) for j in range(4)]
	r.recvuntil("Solve 10 stage to get the flag\n")
	n = int(r.recvline().decode()[:-1].split("n = ")[1])
	e = int(r.recvline().decode()[:-1].split("e = ")[1])
	c = int(r.recvline().decode()[:-1].split("c = ")[1])
	x = int(r.recvline().decode()[:-1].split("x = ")[1])
	y = int(r.recvline().decode()[:-1].split("y = ")[1])

	return_dicts = manager.dict()
	proc = Process(target=solve_equation, args=(x, y, param_input, return_dicts))
	proc.start()
	proc.join(timeout=4)
	proc.terminate()
	if return_dicts["result"]:
		for obj in return_dicts["result"]:
			try:
				p_temp = int(obj[0].rhs())
				q_temp = int(obj[1].rhs())
			except:
				continue
			if p_temp*q_temp == n and isprime(p_temp) and isprime(q_temp):
				break
	else:
		print("loh")

	phi = (p_temp-1)*(q_temp-1)
	d = inverse(e,phi)
	answer = pow(c, d, n)
	r.sendlineafter("Give me decrypted c : ", str(answer))
	print(r.recvline())

print(r.recvuntil("}"))


