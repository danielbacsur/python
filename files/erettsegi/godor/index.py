melyseg = []

with open("melyseg.txt", "r") as forras:

    # 1. FELADAT
    print("1. feladat")
    for s in forras:
        melyseg.append(int(s.strip()))
    print(len(melyseg))

    # 2. FELADAT
    print("2. feladat")
    bemenet = int(input("Adjon meg egy távolságértéket! "))
    print(f"Ezen a helyen a felszín {melyseg[bemenet]} méter mélyen van.")

    # 3. FELADAT
    print("3. feladat")
    szazalek = round(melyseg.count(0) / len(melyseg), 2)
    print(f"Az érintetlen terület aránya {szazalek}%.")

    # 4. FELADAT
    with open("godrok.txt", "w") as godrok:
        szakaszok = [x for x in "".join([str(x) for x in melyseg]).split("0") if x != ""]
        godrok.writelines("\n".join(szakaszok))

        # 5. FELADAT
        print(f"A gödrök száma: {len(szakaszok)}")

    # 6. FELADAT
    print("6. feladat")
    if melyseg[bemenet] == 0:
        print("Az adott helyen nincs gödör.")
    else:
        print("a)")
        kezdete = bemenet
        while melyseg[kezdete] != 0: kezdete -= 1
        vege = bemenet
        while melyseg[vege] != 0: vege += 1
        print(f"A gödör kezdete: {kezdete + 2} méter, a gödör vége: {vege} méter. ")

        print("b)")
        index = bemenet - 1
        flag = False
        while kezdete + 1 < index:
            if(melyseg[index] > melyseg[index+ 1] ):
                print("b", index)
                flag = True
            index -= 1

        index = bemenet - 1

        while index < vege - 1:
            if(melyseg[index- 1]  < melyseg[index]):
                print("a", index)
                flag = True
            index += 1

        print("Folyamatosan mélyül." if flag else"Nem mélyül folyamatosan.")

        print("c)")
        print(f"A legnagyobb mélysége {max(melyseg[kezdete + 1: vege - 1])} méter.")

        print("d)")
        print(f"A térfogata {sum(melyseg[kezdete + 1: vege]) * 10} méter.")



        
