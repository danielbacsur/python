baratok = ["Gizi", "Attila", "Karesz"]
print(baratok)
print(baratok[1])

baratok.append("Livia")
print(baratok)

baratok.remove("Gizi")
print(baratok)

baratok.pop(2)
print(baratok)

# baratok.clear()
# print(baratok)

baratok.sort()
print(baratok)

baratok.reverse()
print(baratok)

masik_lista = baratok.copy()