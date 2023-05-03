import random

val = int(input("Hány alkalommal legyen dobás? "))
lst = [[random.randint(1, 6) for _ in range(3)] for _ in range(val)]

anni, panni = 0, 0

for dobas in lst:
    print("Dobás:", end=" ")
    print(", ".join([str(x) for x in dobas]), end=" ")
    print("=", end=" ")
    print(sum(dobas), end="\t")
    print("Nyert:", end=" ")
    
    if sum(dobas) < 10:
        print("Anni")
        anni += 1
    else:
        print("Panni")
        panni += 1

print(f"A játék során {anni} alkalommal Anni, {panni} alkalommal Panni nyert.")

