from distutils.log import debug
import string
import random

# Vérifier si le mdp contient au moins 2 nombres et une masjuscule
# et s'il fait au moins 8 characteres

length = random.randint(4, 12)

def password_generator(length):
    hexdigits = string.hexdigits
    punctuation = string.punctuation
    char = hexdigits + punctuation
    return "".join(random.choices(char, k=length))

def password_checker(password):
    uppercase = string.ascii_uppercase
    digits = string.digits
    count_uppercase = 0
    count_digits = 0

    for x in password:
        if x in uppercase:
            count_uppercase += 1
        if x in digits:
            count_digits += 1
  
    condition1 = len(password) > 8
    condition2 = count_uppercase >= 1
    condition3 = count_digits >= 2

    if condition1 and condition2 and condition3:
        return "OK"
    else:
        return "Wrong password"


password = password_generator(length)
print(password)

print(password_checker(password))