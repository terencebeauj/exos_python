def somme(a, b):
    minimum = min((a, b))
    maximum = max((a, b))

    numbers = range(minimum, maximum + 1)
    total = 0
    for nombre in numbers:
        total += nombre
    print(total)

somme(100, 200)