from string import digits

def isdigit(nombre):
    if not isinstance(nombre, str):
        return 'Enter a string'
    
    for char in nombre:
        if char not in digits:
            return False
    return True

print(isdigit("1854274"))