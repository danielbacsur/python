# Ugyan az a funkcio mint az elozo feladatban

def prim(x):
    for i in range(2, x):  # Vegigmegy az osszes lehetseges oszton
        if x % i == 0:     # Ha van ilyen oszto, akkor mar nem lehet prim
            return False   # A funkcio megszakad

    return True            # Egyebkent True


val = int(input("Írj be egy pozitív egész számot: "))
lst = []


for i in range(2, val):     # Vegigmegy az osszes lehetseges szamon az adott tartomanyban
    if (prim(i)):           # Ha prim, akkor ...
        lst.append(str(i))  # ... hozzaadja a listahoz (MAR "STRING" KENT!)

# Kiirja a lista elemeit
# Mivel a lista elemei mar STRINGge vannak alakitva, ezert hasznalhatjuk a join funkciot:

print("Ezeket a primeket talaltam: ", ", ".join(lst))
