import string
from tokenize import Double

employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé", "Terence", "Fanny"]

def sort_employes(employe):
    alphabet = string.ascii_lowercase
    middle = int(len(alphabet) / 2)
    first = alphabet[:middle]
    second = alphabet[middle:]
    first_part_employe = []
    second_part_employe = []

    for name in employe:
        if name[0].lower() in first:
            first_part_employe.append(name)
        else:
            second_part_employe.append(name)
    
    first_list = ", ".join(first_part_employe)
    second_list = ", ".join(second_part_employe)

    print("Employés de A a M: " + first_list)
    print("Employés de N a Z: " + second_list )

sort_employes(employes)
