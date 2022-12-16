termekek = [
    ["tea", 110, False],
    ["almale", 130, False],
    ["tej", 250, False],
    ["kakao", 400, False],
    ["vodka", 900, True],
    ["bor", 1100, True],
    ["pezsgo", 1300, True],
    ["palinka", 800, True],
]
kosar = []

print("Koszontelek a boltomban!")
eletkor = int(input("hany eves vagy? "))

while True:
    elerheto = []
    for termek in termekek:
        if eletkor > 18 or not termek[2]:
            elerheto.append(termek[0])

    print("Elerheto termekek:\t", " ".join(elerheto))
    kivalasztott = input("Mit szeretnel? ")

    for termek in termekek:
        if termek[0] != kivalasztott:
            continue

        if eletkor < 18 and termek[2]:
            print("Kiskoru vagy! Alkoholt meg nem vasarolhatsz!")
            continue

        kosar.append(termek)
        print(termek[0], "hozzaadva a kosarhoz.", f"{termek[1]}Ft")

    folytatas = input("Szeretnel mast is? ")
    if folytatas.lower() != "igen":
        break

print("\nVasarolt termekek:")
for termek in kosar:
    print("  " + termek[0].ljust(8), termek[1], "Ft")

print("- - - - - - - - - -")
osszeg = sum([termek[1] for termek in kosar])
print("Osszesen:".ljust(10), osszeg, "Ft")
