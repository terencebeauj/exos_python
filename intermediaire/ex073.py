import string
import random

def password_generator(length):
    hexdigits = string.hexdigits
    punctuation = string.punctuation
    char = hexdigits + punctuation
    return "".join(random.choices(char, k=length))

print(password_generator(8))