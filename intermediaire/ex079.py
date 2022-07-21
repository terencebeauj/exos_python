import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"

def pangramme_checker(phrase):
    phrase = phrase.lower()
    letters = string.ascii_lowercase
    punctuation = string.punctuation
    counter = 0
    array = []
    for char in punctuation:
        phrase = phrase.replace(char,"")

    phrase = phrase.replace(" ", "")
    for letter in phrase:
        if letter not in array and letter in letters:
            counter += 1
        array.append(letter)

    if counter == 26:
        return "Cette phrase est un pangramme"
    return "Cette phrase n'est pas un pangramme"


print(pangramme_checker(phrase))
