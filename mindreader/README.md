# mindreader
###### [Back](../README.md)
###### [Solution](solution.py) 

## Challenge
[source](server.py)  
[connect](connect.sh)  
  

This service allows us to get the flag encrypted with AES-OFB, or any text we choose encrypted with the exact same key and IV.  
Due to the way OFB mode works, if we xor the plaintext with the ciphertext, we
get the key encrypted with the IV. This means we can just xor any plaintext we
choose with the ciphertext of it, and the xor that with the encrypted flag.  
Doing that, we get the flag: `flag{3v3ry_71m3_y0u_th1nk_4_7h0u9h7,u53_4_n3w_IV}`
