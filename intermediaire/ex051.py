employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

i = 1

for x in liste:
    if isinstance(x, str):
        id = f'id-{i:02d}'
        employes[id] = x
        i+=1


print(employes)