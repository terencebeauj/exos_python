def find_divisors(number):
    diviseurs = []
    for x in range(1, number):
        if number % x == 0:
            diviseurs.append(x)
    return diviseurs

print(find_divisors(25))
