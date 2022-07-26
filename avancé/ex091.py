class SuperChaine(object):
    def __init__(self, phrase) -> None:
        self.phrase = phrase
    
    def majuscule(self) -> str:
        return self.phrase.upper()

    def minuscule(self) -> str:
        return self.phrase.lower()

    def titre(self) -> str:
        return self.phrase.capitalize()

chaine = SuperChaine("UdeMy")
print(chaine.majuscule())
print(chaine.minuscule())
print(chaine.titre())