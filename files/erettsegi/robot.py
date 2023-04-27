bemenet = input("Kérem a robot parancsait: ").upper()

e, d, k, n = 0, 0, 0, 0

# e = str.count(bemenet, "E")
# d = str.count(bemenet, "D")
# k = str.count(bemenet, "K")
# n = str.count(bemenet, "N")

for karakter in bemenet:
    if karakter == "E":
        e += 1
    elif karakter == "D":
        d += 1
    elif karakter == "K":
        k += 1
    elif karakter == "N":
        n += 1

x = k-n
y = e-d

if x > 0:
    print("K" * abs(x), end="")
else:
    print("N" * abs(x), end="")

if y > 0:
    print("E" * abs(y), end="")
else:
    print("D" * abs(y), end="")
