import requests
import random

txt = requests.get("https://python.danielbacsur.com/szavak.txt").text
szavak = txt.splitlines()
szo = random.choice(szavak)
kitalalt = []

print("💡\t", szo)

while True:
    tipp = input("✏️\t  ")
    kitalalt.append(tipp)

    valasz = ""

    for betu in szo:
        if betu in kitalalt:
            valasz += betu
        else:
            valasz += "#"

    if "#" in valasz:
        print("👌\t", valasz)
    else:
        print("❤️\t ", valasz.capitalize(), ". Kitaláltad!")
        break

