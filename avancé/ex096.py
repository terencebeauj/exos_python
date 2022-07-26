class Voiture(object):
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur
    
    def __repr__(self):
        return f"Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}$"

super_voiture = Voiture("lamborghini", 150000, "rouge")
print(super_voiture)