
fourth_char = ""
fifth_char = ""
TLS = 0

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
fifth = int(input())

local10 = 0

for i in range(5):
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)
    fdiv = (third + fourth * first) % 32
    first = second // (2 ** fdiv)
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)
    sdiv = (fifth - fourth * first) % 32
    second = fourth * (2**sdiv)
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)
    tdiv = (first + third * second) % 32
    third = fifth // (2 ** tdiv)
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)
    fodiv = (third - fourth * fifth) % 32
    fourth = second * (2 ** fodiv)
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)
    fidiv = (fourth + second * fifth) % 32
    fifth = third // (2 ** fidiv)
    print(first%65536, second%65536, third%65536, fourth%65536, fifth%65536)

    print()

print(first%65536 + second%65536 + third%65536 + fourth%65536 + fifth%65536)

print(0x7a69)

