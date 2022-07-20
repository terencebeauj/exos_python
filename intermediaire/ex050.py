compteur = 0

while True:
    print(f"Le compteur est maintenant a {compteur}.")
    reponse = input("Voulez-vous continuer ? (o/n) ")
    if reponse == "n":
        break
    else:
        compteur += 1