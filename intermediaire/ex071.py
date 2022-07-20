from random import randint

def generate_byte():
   return "".join([str(randint(0, 1)) for _ in range(8)])

print(generate_byte())