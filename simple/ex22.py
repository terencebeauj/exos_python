employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}

# temp1 = employes.get("01", None)

# if temp1 == None:
#     print("La 1ere clé n'existe pas")
#     quit()

# temp2  = temp1.get("identite", None)

# if temp2 == None:
#     print("La 2e clé n'existe pas")
#     quit()

# prenom = temp2.get("prenom", None)

# if prenom == None:
#     print("La 3e clé n'existe pas")
#     quit()

# print(prenom)


## Solution Optimale

print(employes.get("01", {}).get("identite", {}).get("prenom", {}))