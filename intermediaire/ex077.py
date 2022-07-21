phrase = "Bonjour tout le monde"

def reverser(phrase):
    phrase = phrase.lower()
    array = phrase.split()
    array.reverse()
    array[0] = array[0].capitalize()
    return " ".join(array)

print(reverser(phrase))