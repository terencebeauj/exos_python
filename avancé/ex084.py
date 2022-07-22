def join(*args):
    separator = args[0]
    sentence = ""
    for char in args[1:-1]:
        sentence += char
        sentence += separator
    sentence += args[-1]
    return sentence

j = join(":", "Bonjour", "tout", "le", "monde")
print(j)