# traverse_3
###### [Back](../README.md)


Because the regex removes `../` and replaces it with nothing, if we write `....//`,  
it will become `../` after the regex parses it. Therefore, we can go to `/flag.txt`  
by doing `....//....//....//....//....//....//....//flag.txt`.

