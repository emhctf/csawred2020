# apple_cider_vinegar
###### [Back](../README.md)

The challenge gives some encrypted text. Looking at it carefully, we see
something in the format of a flag:  
`ysiy{W1x3r3ro_V1wp3j}`  
Looking at the full text, it seems as though we should use frequency analysis.
However, it is not a plain substitution cipher as `ysiy` corresponds to `flag`,
which cannot occur in plain substitution.  

At this point I was sorta bored, so I searched up `Apple Cider Vinegar` and
found this
[site](https://www.webmd.com/diet/apple-cider-vinegar-and-your-health#1).
Looking at the ciphertext and the first paragraph carefully, we notice that the
spaces match. Assuming it is the plaintext, we can use
[decode.fr](https://www.dcode.fr/vigenere-cipher). Selecting `Knowing
a Plaintext Word` and putting in the longest word, `fermentation`, the
decrypted version spits out and we have the flag.
