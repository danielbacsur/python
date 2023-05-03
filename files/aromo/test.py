grades = {'Kommunikáció': [4, 4, 3, 4, 3, 1], 'Művészetismeret': [2, 4, 4, 5, 5, 4, 1], 'Első idegen nyelv, Angol nyelv': [5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 3], 'Második idegen nyelv, Olasz nyelv': [5, 5, 5, 5], 'Matematika': [3, 5, 5, 5, 5, 5, 5, 5], 'Történelem': [3, 4, 3, 1, 5, 5, 3, 3, 5, 4, 5, 5, 4, 4, 5, 4, 4, 5, 5], 'Természettudomány': [5, 5, 5, 5, 4, 4, 3, 5, 3, 5], 'Földrajz': [3, 5, 5, 5, 4, 5, 4, 5], 'Digitális kultúra': [4, 5, 5, 5], 'Gazdasági ismeretek': [2, 3, 4]}

summed = [sum(x) / len(x) for x in list(grades.values())]

print(sum(summed) / len(summed))
# print(sum(list(grades.values())))
# print(sum(grades.values()))