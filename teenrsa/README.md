# teenrsa
###### [Back](../README.md)

## Challenge
[source](teenrsa.py)  
[output](output.txt)
  

Inspecting the source, you see that multiplying two 1024 bit primes would
create a value of `n` too large to mod the ciphertext at all. By just cube
rooting, we get the flag: `flag{where_did_my_primes_go?}`
