import string

alphabet = string.ascii_lowercase

my_dict = {x: y for x, y in zip(range(1, len(alphabet)+1), alphabet)}

print(my_dict)

