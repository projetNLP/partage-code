from PIL import Image, ImageTk
from appJar import gui

import model

app = gui("interface", "1000x700")
Q = model.lire_fichier()[1]
L = model.lire_fichier()[2]

def suivant():
    L = [app.getOptionBox(f"{i}") for i in range(5)]
    image_path = model.retrouve_image()
    model.enregistre_reponse(image_path, L)
    image = Image.open(model.lire_fichier()[0] + '/' + model.retrouve_image())
    image_resize = ImageTk.PhotoImage(image.resize((600, 600)))
    app.setImageData("pic", image_resize, fmt="PhotoImage")
    app.clearAllOptionBoxes()
    
def precedent():
    image = model.image_precedente(model.retrouve_image())
    image_precedent = Image.open(model.lire_fichier()[0] + '/' + image)
    model.change_commente(image)
    image_resize = ImageTk.PhotoImage(image_precedent.resize((600, 600)))
    app.setImageData("pic", image_resize, fmt="PhotoImage")

def interface(image_resize, Q, L):
    app.setFont(size=25, family="Arial", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', fg='black'):
        app.addLabel("en-tête", "Outil de classification d'images")
        app.setLabelBg("en-tête", "indianred")
        app.setLabelFg("en-tête", "Snow")
        app.setLabelHeight("en-tête", 1)
        app.addImageData("pic", image_resize, fmt="PhotoImage")
        app.addButton("Precedent", precedent)
        app.setButtonBg("Precedent", "PowderBlue")
        app.setButtonFg("Precedent", "black")
        app.setButtonWidth("Precedent", 5)
        app.setButtonHeight("Precedent", 1)

    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
            app.setLabelBg(Q[x], "bisque")

        app.addButton("Suivant", suivant)
        app.setButtonFg("Suivant", "white")
        app.setButtonBg("Suivant", "RoyalBlue")
        app.setButtonWidth("Suivant", 5)
        app.setButtonHeight("Suivant", 1)

    app.go()

# model.init_annotation() # n'utiliser cette ligne que pour la première fois d'annotation pour un répertoire d'images
image = Image.open(model.lire_fichier()[0] + '/' + model.retrouve_image())
image_resize = ImageTk.PhotoImage(image.resize((600, 600)))
interface(image_resize, Q, L)
