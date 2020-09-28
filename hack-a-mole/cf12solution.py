from pwn import *
import re

p = remote('web.red.csaw.io', 5016)
p.recvline()
box_width = 17
box_height = 8
divider_chars = ['0', '|', "*", ' ', 'O', '-', '.', '+', "@", "#", '[', ']']
nope = ['']
hard_part = False
right_in_a_row = 0
flag_inc = False
while True:
    content = p.recvuntil("(row col):").decode('utf-8')
    if "Score: 9950" in content:
        flag_inc = True
    print(content)
    content = content.split('\n')[2:] # get rid of score and whitespace
    start_count = False
    counter = 1

    print("Started finding num spaces between boxes")
    for i, line in enumerate(content):
        print(line)
        if line.strip() == '' and start_count:
            print("Added one to count")
            counter += 1
        elif line.strip() == '':
            print("Started count")
            start_count = True
        elif start_count: # its not a newline and we already started counting
            spaces_vertical = counter
            print("Got vertical spaces")
            break
    '''
    spaces_horizantal = 0
    for i, char in enumerate(content[2]): # just choose a line that's not the first line of a box divider or whitespace
        if i >= box_width - 1: # check if we reached the first whitespace after the edge of the first box
            spaces_horizantal += 1
        if char != " " and spaces_horizantal > 0: # check if we started counting already and break if we reached the border of the next box
            break
    print(f"Horizantal spaces: {spaces_horizantal} Vertical spaces: {spaces_vertical}")
    '''
    if not hard_part:
        spaces_horizantal = 2
    else:
        spaces_horizantal = int(input("Enter the number of horizantal spaces: "))
        spaces_vertical = int(input("Enter the number of vertical spaces: "))
    try:
        for i, line in enumerate(content):
            for i2, char in enumerate(line):
                if not char in divider_chars and " ___ " in line and char == "_":
                    # account for space below box
                    row = str(int(i / (box_height + spaces_vertical)))
                    # 17 + 2 to account for spaces between boxes and the divider of the next box
                    col = str(int(i2 / (17 + spaces_horizantal)))
                    payload = f"{row} {col}"
                    print(payload)
                    p.sendline(payload)
                    raise Exception("found")
    except:
        pass
    result = p.recvline()
    print(result)
    if result != b' Whack!\n':
        hard_part = True
    else:
        right_in_a_row += 1
    if right_in_a_row > 1:
        hard_part = False
    if flag_inc:
        p.interactive()
p.interactive()