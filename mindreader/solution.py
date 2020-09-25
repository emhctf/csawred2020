import base64

print("nc crypto.red.csaw.io 5011")
print("idk for some reason it doesn't work on pwntools :(")

plaintext = b"\x01"*63

afterpad = b"\x01"*64

given_input = base64.b64encode(plaintext)

print("Give input (ask about something else) : ", end="")
print(given_input)

encrypted_plaintext = base64.b64decode("1mck6zrl/nWNUY243rgB5O65LB50vPGOBAEwNN3etlgMfwzQQ5bo8iNN6wCIm+tlb0jVhCVUV1syUHgsOwoePQ==")

enc_flag = base64.b64decode("sQpEjUDXiUf+KdOO7tQzupaIWEAB1cHhbl8Fauu3hyw0Fjr9N6LarBYThDL+xaMyE0bbiitaWVU8XnYiNQQQMw==")


key = bytes([ a ^ b for (a,b) in zip(encrypted_plaintext, afterpad)])

flag = bytes([ a ^ b for (a,b) in zip(key, enc_flag)])

print(flag)
