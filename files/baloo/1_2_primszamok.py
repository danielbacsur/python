val = int(input("Írj be egy pozitív egész számot: "))

# Egy funkcio, ami True ha a megadott szam prim. Ha nem prim, akkor a visszakuldott ertek False

def prim(x):
    for i in range(2, x):  # Vegigmegy az osszes lehetseges oszton
        if x % i == 0:     # Ha van ilyen oszto, akkor mar nem lehet prim
            return False   # A funkcio megszakad

    return True            # Egyebkent True


if val == 1 or prim(val):  # Ha a szam egy vagy a prim() erteke True lesz, ...
    print("Prim")
else:                      # Ha a prim() erteke False lesz, ...
    print("Nem prim")
