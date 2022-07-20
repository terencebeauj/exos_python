def find_divisble_by_7_and_not_multiple_of_3(nombre):
    numbers = []
    for x in range(1, nombre + 1):
        if x % 7 == 0 and x % 3 != 0:
            numbers.append(x)
    return numbers

print(find_divisble_by_7_and_not_multiple_of_3(1000))