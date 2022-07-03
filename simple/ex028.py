import os

fichier = "C:/Python36/python.exe"

print(os.path.splitext(fichier)[1].replace(".", ""))