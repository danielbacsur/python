class Epitmeny():
    def __init__(self, adatok):
        self.adoszam = int(adatok[0])
        self.utca = adatok[1]
        self.hazszam = adatok[2]
        self.adosav = adatok[3]
        self.terulet = int(adatok[4])
    
def ado(prices, adosav, terulet):
    val = prices[["A", "B", "C"].index(adosav)] * terulet
    return 0 if val < 10000 else val

with open("C:\\Users\\conta\\Documents\\Projects\\python\\files\\erettsegi\\epitmenyado\\utca.txt", "r") as file:
    prices = file.readline().split(" ")
    prices = [int(x) for x in prices]
    epitmenyek = []
    for row in file:
        if row.strip() != "...":
            epitmenyek.append(Epitmeny(row.strip().split(" ")))

    print(f"2. feladat. A mintában {len(epitmenyek)} telek szerepel.")

    harmadik_adoszam = int(input("3. feladat. Egy tulajdonos adószáma: "))
    harmadik_talalatok = list(filter(lambda x: x.adoszam == harmadik_adoszam, epitmenyek))
    if len(harmadik_talalatok) == 0:
        print("Nem szerepel az adatállományban.")
    else:
        for epitmeny in harmadik_talalatok:
            print(f"{epitmeny.utca} utca {epitmeny.hazszam}")

    print("5. feladat")
    for char in ["A", "B", "C"]:
        summ, numm = 0, 0
        for epitmeny in epitmenyek:
            if epitmeny.adosav == char:
                numm += 1
                summ += ado(prices, char, epitmeny.terulet)

        print(f"{char} sávba {numm} telek esik, az adó {summ} Ft.")

    print("6. feladat. A több sávba sorolt utcák: ")
    for utca in list(dict.fromkeys([x.utca for x in epitmenyek])):
        if 2 <= len(list(filter(lambda x: (x.utca == utca), epitmenyek))):
            print(utca)
        
    with open("fizetendo.txt", "w") as fizetendo:
        for tulaj in list(dict.fromkeys([x.adoszam for x in epitmenyek])):
            val = sum([ado(prices, x.adosav, x.terulet) for x in list(filter(lambda x: (x.adoszam == tulaj), epitmenyek))])
            fizetendo.write(f"{tulaj} {val}\n")