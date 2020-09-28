from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import binascii
import base64 as b64




iv = os.urandom(16)


enc = b64.b64decode(input("Encrypted: "))

pt = iv + b"Your application has been REJECTED"

k = bytes([a^b for (a,b) in zip(pt, enc)])

act = iv + b'Your application has been ACCEPTED'

token = b64.b64encode(bytes([a^b for (a,b) in zip(k, act)]))
print(token)
