prenom = "Pierre"

# INSÉRER VOTRE CONDITION ICI.
# Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère. Ici c'est le cas,
# votre condition doit donc être vraie et printer la phrase "La variable est une chaîne de caractères".

if type(prenom) == str:
    print("La variable est une chaine de caracteres")
else:
    print("La variable n'est pas une chaine de caracteres")

prenom = 0

# INSÉRER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas égale à une chaîne de caractère. Votre condition doit donc être fausse et 
# la phrase ne doit pas s'afficher.

if type(prenom) == str:
    print("La variable est une chaine de caracteres")
else:
    print("La variable n'est pas une chaine de caracteres")
