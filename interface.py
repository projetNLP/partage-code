from PIL import Image, ImageTk
from appJar import gui
from tkinter import Toplevel
from tkinter.constants import TOP, UNDERLINE
from tkinter.font import families
from appJar import gui
import model
app = gui("interface", "1000x700")
# pour accéder au répertoire d'image avec appjar utiliser: .setImageLocation(location)

def suivant(btn):
    print(app.getOptionBox("1"))


def interface(image, Q, L):
    app.setFont(size=20, family="Pumpkin Soup", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', sticky='NEW', stretch='COLUMN'):
        app.addLabel("en-tête", "outil de classification d'images")
        app.addImageData("pic", image, fmt="PhotoImage")
        app.setImageSize("pic", 100, 690)
        # app.addButton("Précédent", press_precedent)
        # app.setSize("Fullscreen")
    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
        app.addButton("Suivant", suivant)
    app.go()

model.init_annotation()
image = ImageTk.PhotoImage(Image.open(model.lire_fichier()[0] + '/' + model.retrouve_image()))
Q = model.lire_fichier()[1]
L = model.lire_fichier()[2]
interface(image, Q, L)
