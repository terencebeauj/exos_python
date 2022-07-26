class Voiture():
    def __init__(self, marque, prix, couleur) -> None:
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture.marque)
print(super_voiture.prix)
print(super_voiture.couleur)
