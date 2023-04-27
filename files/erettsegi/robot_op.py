val = list(input("Kérem a robot parancsait: "))

while "E" in val and "D" in val:
    val.remove("E")
    val.remove("D")

while "K" in val and "N" in val:
    val.remove("K")
    val.remove("N")

val.sort(reverse=True)
print("".join(val))