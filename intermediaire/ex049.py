nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

numbers = []

for x in nombres:
    if x not in numbers:
        numbers.append(x)

print(numbers)
