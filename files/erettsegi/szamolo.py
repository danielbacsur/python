import random

print('''
Milyen műveletet szeretne gyakorolni?

1. Összeadás
2. Kivonás
3. Szorzás
''')

valasz = int(input("Választás (1-3): "))

db, ok = 0, 0

while ok < 5:
    db += 1
    a, b = random.randint(1, 10), random.randint(1, 10)
    c, d = 0, 0

    if valasz == 1:
        print(f'{a} + {b}', '=', end=" ")
        d = a + b
    elif valasz == 2:
        print(f'{a} - {b}', '=', end=" ")
        d = a - b
    elif valasz == 3:
        print(f'{a} * {b}', '=', end=" ")
        d = a * b

    c = int(input())

    print('\033[{}C\033[1A'.format(14), end="")

    if c == d:
        ok += 1
        print("Helyes!")
    else:
        print("Hibás!")

print(f'''
Gratulálunk!

Sikerült 5 helyes műveletet elvégezni {db} próbálkozásból.
''')