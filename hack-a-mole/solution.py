from pwn import *
import re
from itertools import *

io = remote("web.red.csaw.io", 5016)

LINE_PATTERN = re.compile(rb"^.*(.)\1{10}.*$", re.MULTILINE)
CELL_PATTERN = re.compile(rb"(\S).{12,15}\1|<.{12,15}>|\[.{12,15}\]|\/.{9,15}\\|\\.{9,15}\/")
MOLE_HEAD = b"  ___  "

def get_col(row):
    print(row)
    matches = CELL_PATTERN.finditer(row)
    enumerated = enumerate(matches)
    filtered = filter(lambda x: MOLE_HEAD in x[1].group(), enumerated)
    return next(filtered)[0]

def get_coords(output):
    matches = LINE_PATTERN.finditer(output)
    matched_strings = map(lambda x: x.group(), matches)
    prefiltered = list(filter(lambda x: x.strip(), matched_strings))
    deduplicated = map(lambda x: next(x[1]), groupby(prefiltered, lambda x: x == prefiltered[0])) # alternate separators and non-separators
    filtered = list(filter(lambda x: x != prefiltered[0], deduplicated)) # then filter out the separator rows
    print(filtered)
    for i, x in enumerate(filtered):
        if MOLE_HEAD in x:
            return i, get_col(x)

try:
    while True:
        output = io.recvuntil("Whack (row col): ")
        print(output.decode())
        row, col = get_coords(output)
        print(row, col)
        io.sendline(str(row) + " " + str(col))
except EOFError:
    print(io.recv())


