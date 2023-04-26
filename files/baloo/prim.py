val = int(input("ASD: "))

def prim(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if val == 1 or prim(val):
    print("Prim")
else:
    print("Nem prim")


