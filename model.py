import json
import os

#lire le fichier json
def lire_fichier():
    with open('test_config.json', "r") as f:
        donnee = json.load(f)
        liste1 = []
        liste2 = []
        image = donnee[num_image]
        for keys in image:
            liste2.append(keys)
        liste1.append(liste2[0])
        liste1.append(liste2[1])
        liste2.pop(0)
        liste2.pop(1)
    return liste1, liste2

#retourne le nom et l'emplacement des images
#pour accéder au répertoire d'image avec appjar utiliser: .setImageLocation(location)
def lire_emplacement():
    return lire_fichier()[0]

#lire les questions
def lire_question():
    return lire_fichier()[1]

#renvoie une liste des noms d'images
def recupere_image():
    return os.walk(lire_emplacement()[1]).next()[2]
