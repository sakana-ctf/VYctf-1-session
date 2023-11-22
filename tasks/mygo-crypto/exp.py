from pwn import *
ciphertext = []
p = remote("47.113.145.248" , 32123)
#p = remote("127.0.0.1" , 11111)
# Send 40 null bytes (flag is 40 characters long)
p.sendlineafter(":","00"*40)
for i in range(256):
	p.recvuntil(":")
	ciphertext.append(p.recvuntil('\n')[:-1])

p.recvuntil(":")
flag = p.recvuntil('\n')[:-1]
# XOR all ciphertext with the encrypted flag 
for c in ciphertext:
	f = xor(bytes.fromhex(c.decode()),bytes.fromhex(flag.decode()))
	if f.startswith(b"VYctf{"):
		print(f)
