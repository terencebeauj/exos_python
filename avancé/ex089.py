def recuperer_item(liste, index):
    try:
        return liste[index]
    except:
        return f"Index {index} hors de la liste"

liste = ["Julien", "Marie", "Pierre"]

print(recuperer_item(liste, 0))
print(recuperer_item(liste, 5))
print(recuperer_item(liste, -13))