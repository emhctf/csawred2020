# cracked
###### [Back](../README.md)

This was a really interesting multi-layer rev challenge.

When I started looking through the binary in Ghidra after auto-analysis,
I saw a main function that allocated some memory with `mmap`,
filled part of it with user input, and then passed it to another function.
It then checked the return value of the function, and printed a
success message if the return value was non-zero.

I then looked at the callee function and saw that it was a huge, tangly mess
of code, so I decided to first take a look at the other functions it called.

The first one was a pure, recursive function. I was able to simplify it a lot,
but I still wasn't sure what its goal was. So I copied the code into repl.it
(both the old and the new version to make sure they matched up, which I'm glad
I did, since I caught a bug that way). Since the function took in 2 parameters,
I decided to try keeping one, which was the recursion depth, fixed to values
starting at zero, and setting the 2nd to a large power of 10 to make noticing
patterns easier.  I determined that the formula was 3 to the power of the
recursion depth, times the 2nd parameter, plus some mysterious coefficint
based on the depth. Specifically, the coefficients were
`0, 6, 36, 162, 648, 2430, 8748`, etc. I first tried plugging them into OEIS's
search engine but got no results. I then tried using a normal search engine and
found a result from a math-test-help website, crackmytest.com. It suggested
the formula `2*x*(3**x)`, which I verified with more terms, and was correct!

I then plugged in the parameters used in the big function (which was the
only caller other than itself), and noticed that when implementing the
formula, which involved exponentiation, in C, I got `-0x80000000`,
which seemed like some sort of overflow. It turned out that the function
(technically a macro) I was using operated on floats, so it presumably
just saturated to `INT_MAX`, then overflowed. I then tried evaluating
it using Python and got a huge value, of which I only needed the last byte.
(I was unable to use the recursive version, since it recursed twice per depth,
and the input depth was relatively big, making 2 to the power of it extremely
gynormous.)

I eventually realized that the result of the function didn't actually matter,
but oh well. Additionally, the caller knew that the function ignored the
RDX register, but Ghidra thought it was an extra return value, so I had to
set the calling convention to "syscall".

The other function took in a `char`, compared it to `'d'` and `'e'`, and
returned one of three pointers.

I then went back to analyzing the big function, and saw that the function
was branching based on a byte value from some pointer that was being
incremented by varying amounts, in addition to other byte values.
After analyzing the first few branches, I thought it was just
copying values around in different ways. I eventually realized,
after seeing operations such as XOR and multiplication, that the function
was some sort of bytecode interpreter. I also eventually figured out that
the `mmap`'d parameter was the program's memory, and that the code was copied
out of a constant in the program. I also figured out that the pointer-returning
function, in addition to a conditional repeated outside the function, returned
a pointer to a global representing a register. I began disassembling the
bytecode in Ghidra, assigning types, including an enum I made with all the
possible instructions, but then realized that that would take way too long.
I considered making a Ghidra script, but decided that a standalone Python
script would be much easier and simpler.

It turned out that the program had 2 sections.

The first section consisted of initializing a couple registers, followed by
writing hardcoded byte values into successive memory addresses.

The second section consisted of comparing parallel arrays of values.
The first was the data initialized in the first section.
The second was the user input.
The code checked that, for each index, `(input[i] * 3) ^ (i + 0x64) == data[i]`.
I double checked the first couple characters of `flag`, then wrote a bit of
Python code to brute-force the remaining values. I decided to use regexr.com
to extract the values from the first part of the code, but I initially forgot
to include hex digits, and since the formula is position-dependent, only the
first few characters worked out, coinciding with `flag{`. Once I fixed that,
I finally got the flag: `flag{m0m:w3_h4v3_v1rtu4l1z3r_4t_h0m3}`.

# Files

- [`cracked`](cracked): the provided binary
- [`cracked.py`](cracked.py): my disassembler script
- [`cracked.txt`](cracked.txt): the disassembly from my script
- [`decryptor.py`](decryptor.py): my final bit of Python code to get the flag
