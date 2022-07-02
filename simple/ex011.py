a = 12

if isinstance(a, (int, float)):
    if a > 10:
        print("a est plus grand que 10")
    else:
        print("a est plus petit que 10")
else:
    print("a n'est pas un nombre")