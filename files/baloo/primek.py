def prim(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

val = int(input("ASD: "))
lst = []

for i in range(2, val):
    if(prim(i)):
        lst.append(str(i))

print("Ezeket a primeket talaltam: ", ", ".join(lst))