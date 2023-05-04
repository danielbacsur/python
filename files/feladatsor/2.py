lst = []

for _ in range(3):
    lst.append(int(input()))

if lst[0] == lst[1] and lst[1] == lst[2]:
    print("Ugyan olyan")
else:
    print("Kulonbozo")
