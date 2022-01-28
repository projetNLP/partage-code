import json
import os

def lire_fichier():
    with open('config.json', "r") as f:
        donnee = json.load(f)
        path = donnee["path"]
        liste_questions = [donnee[i] for i in donnee if i[0] == 'q']
        liste_reponses = [donnee[i] for i in donnee if i[0] == 'r']
        for i in range(len(liste_reponses)):
            liste_reponses[i] = liste_reponses[i].split('\\')
    return path, liste_questions, liste_reponses

# retrouver l'image non commenté
def retrouve_image():
    with open('annotation.json', "r") as f:
        liste_images = json.load(f)
    for img in liste_images:
        if liste_images[img]["commenté"] == False:
            return img

def image_precedente(image):
    liste_image = os.walk(lire_fichier()[0]).__next__()[2]
    try:
        for i in range(len(liste_image)):
            if liste_image[i] == image:
                return liste_image[i-1]
    except: 
        print("image non trouvable.")

def change_commente(image):
    with open('annotation.json', "r") as f:
        liste_images = json.load(f)
    donnee = liste_images[image]
    donnee["commenté"]=False



# enregistre les reponses dans le fichier annote, à faire appeler dans l'interface, img est l'entrée de def interface(imge, Q, L)
def enregistre_reponse(img, L):
    with open('annotation.json', "r") as f:
        liste_images = json.load(f)
    if len(L) == 5:
        try:
            for count, reponse in enumerate(L):
                liste_images[img][f"réponse {count + 1}"] = reponse
            liste_images[img]["commenté"] = True
        except:
                print("Cette image d'existe pas.")
    else:
        print("La longueur du paramètre L n'est pas correcte (5).")

    with open('annotation.json', "w") as f:
        json.dump(liste_images, f, indent=4)

def init_annotation(): # initialiser un dossier d'images avec les même questions enregistrées dans config.json
    dict_json = {}
    dict = {
        "commenté": False,
        "question 1": "",
        "réponse 1": "",
        "question 2": "",
        "réponse 2": "",
        "question 3": "",
        "réponse 3": "",
        "question 4": "",
        "réponse 4": "",
        "question 5": "",
        "réponse 5": ""
    }
    for count, question in enumerate(lire_fichier()[1]): #on met toutes les images dans le dictionnaire avec le dictionnaire des questions comme un sous-dictionnaire
        dict[f"question {count + 1}"] = question
    for img in os.listdir(lire_fichier()[0]):
        dict_json[img] = dict
    
    with open('annotation.json', "w") as f:
        json.dump(dict_json, f, indent=4)