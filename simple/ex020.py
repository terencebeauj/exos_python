liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
liste_03 = list()

for i in liste_01:
    if i in liste_02:
        liste_03.append(i)

print(liste_03)
