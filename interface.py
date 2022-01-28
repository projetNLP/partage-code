from PIL import Image, ImageTk
from appJar import gui
import model

app = gui("interface", "1000x700")


def suivant():
    L = [app.getOptionBox(f"{i}") for i in range(5)]
    image_path = model.retrouve_image()[0]
    model.enregistre_reponse(image_path, L)
    app.stop()


def interface(image_resize, Q, L):
    app.setFont(size=20, family="Verdana", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', sticky='NEW', stretch='COLUMN'):
        app.addLabel("en-tête", "outil de classification d'images")
        app.setLabelBg("en-tête", "DarkCyan")
        app.setLabelHeight("en-tête", 2)
        app.addImageData("pic", image_resize, fmt="PhotoImage")

    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
            app.setLabelBg(Q[x], "bisque")

        app.addButton("suivant", suivant)
        app.setButtonFg("suivant", "white")
        app.setButtonBg("suivant", "limegreen")
        app.setButtonWidth("suivant", 10)
        app.setButtonHeight("suivant", 1)

    app.go()

model.init_annotation() # n'utiliser cette ligne que pour la première fois d'annotation pour un répertoire d'images
Q = model.lire_fichier()[1]
L = model.lire_fichier()[2]
for img in model.retrouve_image():
        image = Image.open(model.lire_fichier()[0] + '/' + img)
        image_resize = ImageTk.PhotoImage(image.resize((600, 600)))
        interface(image_resize, Q, L)
