val = int(input("Írj be egy pozitív egész számot: "))

lst = []

for i in range(1, val+1):
    if val % i == 0:
        lst.append(str(i))

print(val, " Osztói: ", "; ".join(lst))