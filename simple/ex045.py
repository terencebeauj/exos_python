nombres = range(50)
nombres_pairs = []

for i in list(nombres):
    if i%2 == 0:
        nombres_pairs.append(i)

print(nombres_pairs)