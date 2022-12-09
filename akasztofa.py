import requests
import random

txt = requests.get("https://python.danielbacsur.com/szavak.txt").text
szavak = txt.splitlines()
szo = random.choice(szavak)
kitalalt = []

print(szo)

while True:
    tipp = input("💡 ")
    kitalalt.append(tipp)

    valasz = ""

    for betu in szo:
        if betu in kitalalt:
            valasz += betu
        else:
            valasz += "#"

    if not "#" in valasz:
        print("Kitaláltad! ❤️")
        break

    print(valasz)
