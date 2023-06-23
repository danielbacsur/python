tabla = [[0 for _ in range(9)] for _ in range(9)]
lepesek = []

def resztabla(sor, oszlop):
    return 1 + sor // 3 * 3 + oszlop // 3

if __name__ == "__main__":

    # 1. FELADAT
    print("1. feladat")
    fajl = input("Adja meg a bemeneti fájl nevét! ")
    sor = int(input("Adja meg egy sor számát! ")) - 1
    oszlop = int(input("Adja meg egy oszlop számát! ")) - 1

    # 2. FELADAT
    with open(fajl, "r") as fajl:
        for i, s in enumerate(fajl):
            if i < 9: tabla[i] = s.strip().split(" ")
            else: lepesek.append(s.strip().split(" "))
    
    # 3. FELADAT
    print("\n3. feladat")
    cella = tabla[sor][oszlop]
    if cella == "0":
        print("Az adott helyet még nem töltötték ki.")
    else:
        print(f"Az adott helyen szereplő szám: {cella}")
        print(f"A hely a(z) {resztabla(sor, oszlop)} résztáblázathoz tartozik. ")

    # 4. FELADAT
    print("\n4. feladat")
    nullak = sum(x.count("0") for x in tabla)
    szazalek = round(nullak / (9 * 9) * 100, 1)
    print(f"Az üres helyek aránya: {szazalek}%")

    # 5. FELADAT
    print("\n5. feladat")
    for lepes in lepesek:
        sor, oszlop, szam = int(lepes[1]) - 1, int(lepes[2]) - 1, lepes[0]
        print(f"A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szam}")

        if tabla[sor][oszlop] != "0":
            print("A helyet már kitöltötték")
        elif szam in tabla[sor]:
            print("Az adott sorban már szerepel a szám")
        elif szam in [x[oszlop] for x in tabla]:
            print("Az adott oszlopban már szerepel a szám")
        elif any([szam in x[oszlop // 3 * 3:oszlop // 3 * 3 + 3] for x in tabla[sor // 3 * 3:sor // 3 * 3 + 3]]):
            print("Az adott résztáblázatban már szerepel a szám")
        else:
            print("A lépés megtehető")

        print()