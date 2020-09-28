# prettyplease
###### [Back](../README.md)
###### [Solution](solution.py)

## Challenge
[source](server.py)  
[connect](connect.sh)  
  

Starting off, we see that it uses AES-CTR, another one of those AES stream
ciphers. Looking carefully at the code, w see that it always returns `b"your
application has been REJECTED".`  
We also see that the when encrypting a message, they append the IV on the front
for decryption. If we ask for any arbitrary message, and then take the output
and xor it with the rejected message, we should get the key. By generating
a random IV, appending it to the IV, and xoring it with the accepted message,
it should give us the flag.  
Doing this in a [script](solution.py), we get:
`flag{w3_n33d_m0r3_1n739r17y_1n_7h3_r3v13w_pr0c355}`
