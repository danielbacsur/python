import random
ered = ['alma', 'korte', 'haha']
szo = random.choice(ered)
print(szo)

kitalalt = []

while True:
    b = input(">> ")[0]
    if b in szo:
        kitalalt.append(b)
    
    line = ""
    for i in szo:
        if i in kitalalt:
            line += i
        else:
            line += "#"
    
    breakk = True
    for i in line:
        if i == "#":
            breakk = False
    print(line)
    
    if breakk:
        print("nyertel")
        break