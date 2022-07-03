# 0 -> 2ans: age chien = age * 10.5
# > 2ans: age chien = 21 + (age - 2) * 4

while True:
    age = input("Entrez l'âge du chien: ")

    try:
        age = float(age)
    except:
        print("Entrez un nombre")
        continue

    if age > 0:
        age_en_humain = 10.5*age if age <= 2 else 21 + (age-2)*4
        print(f"L'âge du chien en année humaine est: {age_en_humain:.2f}ans.")
        break
