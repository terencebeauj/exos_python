dictionnaire = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

def get_value(dico, *args):
    if args[0] not in dico.keys():
        return args[-1]


# a = get_value(dictionnaire, "01", "identite", "prenom", "valeur inconnue")