import requests
import random

# Szavak letoltese & random szo kivalasztasa
txt = requests.get("https://python.danielbacsur.com/files/akasztofa/szavak.txt").text
szavak = txt.splitlines()
szo = random.choice(szavak)
kitalalt = []

# Valasztott szo kiirasa *csak segitseg keppen*
print("💡\t", szo)

# Kerdezo vegtelen ciklus
while True:
    # Tipp bekerese es hozzaadasa az eddigi tippekhez
    tipp = input("✏️\t  ")
    kitalalt.append(tipp)

    valasz = ""  # Valtozo letrehozasa a valasz szamara

    # Ciklus a kivalasztott szoban szereplo betuk ellenorzesere
    for betu in szo:
        if betu in kitalalt:  # Ha a betu syerepel a kitalaltak kozott, akkor megmutathatjuk a valaszban
            valasz += betu
        else:  # Ha nem szerepel, akkor takarjuk ki egy statikus karakterrel. Monjuk # vagy ?
            valasz += "#"

    if "#" in valasz:  # Ha tovabbra is szerepel a valaszban ismeretlen karakter, akkor folytassuk a tippelest
        print("👌\t", valasz)
    else:  # Amennyiben kitalaltuk az osszes karaktert akkor, lepjunk ki a ciklusbol, es gratulaljunk a jatekosnak
        print("❤️\t ", valasz.capitalize(), "- Kitaláltad!")
        break
