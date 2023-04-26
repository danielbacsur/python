val = int(input("ASD: "))

lst = []

for i in range(1, val+1):
    if val % i == 0:
        lst.append(str(i))

print("; ".join(lst))