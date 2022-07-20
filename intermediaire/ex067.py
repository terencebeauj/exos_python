def factorial(number):
    if number == 0:
        return 1
    
    multiplier = 1
    for x in range(1, number+1):
        multiplier *= x
    return multiplier

print(factorial(10))
