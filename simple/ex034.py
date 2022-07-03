import random

mot = "Bonjour"

list_mot = [_ for _ in mot.lower()]

random.shuffle(list_mot)

print("".join(list_mot).capitalize())