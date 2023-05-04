with open("C:\\Users\\conta\\Documents\\Projects\\python\\files\\feladatsor\\29\\temp.txt", "r", encoding="utf-8") as file:
    if "Debrecen" in file.read():
        print("Van benne")
    else:
        print("Nincs benne")