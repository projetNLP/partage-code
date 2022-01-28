from PIL import Image, ImageTk
# from ast import Break
from appJar import gui
# from tkinter import Toplevel
# from tkinter.constants import TOP, UNDERLINE
# from tkinter.font import families
import model

app = gui("interface", "1000x700")
image = ImageTk.PhotoImage(Image.open(
    model.lire_fichier()[0] + '/' + model.retrouve_image()))

def suivant(image):
        # R = [True]
        L = []
        for x in range(len(Q)):
            L.append(app.getOptionBox(str(x)))
        model.enregistre_reponse(image, L)
        img = ImageTk.PhotoImage(Image.open(
            model.lire_fichier()[0] + '/' + model.retrouve_image()))
        app.reloadImageData("pic", img, fmt="PhotoImage")

def retour():
        R = [False]
        print(R)

def interface(image, Q, L):
    app.setFont(size=20, family="Verdana", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', sticky='NEW', stretch='COLUMN'):
        app.addLabel("en-tête", "outil de classification d'images")
        app.setLabelBg("en-tête", "DarkCyan")
        app.setLabelHeight("en-tête", 2)
        app.addImageData("pic", image, fmt="PhotoImage")
        app.setImageSize("pic", 100, 600)

        app.addButton("Retour", retour)
        app.setButtonFg("Retour", "white")
        app.setButtonBg("Retour", "firebrick")

    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
            app.setLabelBg(Q[x], "bisque")

        app.addButton("suivant", suivant(image))
        app.setButtonFg("suivant", "white")
        app.setButtonBg("suivant", "limegreen")
        app.setButtonWidth("suivant", 10)
        app.setButtonHeight("suivant", 1)

    app.go()


Q = model.lire_fichier()[1]
L = model.lire_fichier()[2]
interface(image, Q, L)
