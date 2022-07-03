liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

new_liste = [nouveau_nom if nom == nom_a_chercher else nom for nom in liste]

print(new_liste)

new_liste_2 = [nom.replace(nom_a_chercher, nouveau_nom) for nom in liste]

print(new_liste_2)