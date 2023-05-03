val = int(input("Befogó max hossza: "))
lst = []

# A befogo minimum hossza 5, ezert csak annyiszor futtatjuk, ahanyszor megvan benne
# De mivel a szorzo 1-tol kezdodik, igy a "vege" indexhez is hozza kell adni egyet

for i in range(1, val // 5 + 1):
    szharmas = [3 * i, 4 * i, 5 * i]  # Hozzaadjuk az elso variaciot
    lst.append(" ".join(szharmas))

    szharmas = [4 * i, 3 * i, 5 * i]  # Hozzaadjuk a masodik variaciot
    lst.append(" ".join(szharmas))

print("; ".join(lst))  # Eredmeny kiirasa, pontosvesszovel elvalasztva



