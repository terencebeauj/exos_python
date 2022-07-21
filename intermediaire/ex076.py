
from array import array


phrase = "Phrase en camel case"

def convert_to_camel_case(sentence):
    array = sentence.lower().split()
    minuscule = []
    minuscule.append(array[0])
    majuscule = []
    for word in array[1:]:
        majuscule.append(word.capitalize())
    return "".join(minuscule + majuscule)

print(convert_to_camel_case(phrase))