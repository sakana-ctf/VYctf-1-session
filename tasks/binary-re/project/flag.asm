section .text
	global _start

_start:
	mov eax,4
	mov ebx,1
	mov ecx,msg
	mov edx,8
	int 0x80
	mov eax,1
	int 0x80
msg:
	db "flag is:"
