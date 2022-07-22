import os
from string import ascii_lowercase

os.mkdir("./alphabet")

for letter in ascii_lowercase:
    os.mkdir(f"./alphabet/{letter}")