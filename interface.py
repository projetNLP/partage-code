from PIL import Image, ImageTk
from appJar import gui
import model

app = gui("interface", "1000x700")


def suivant(image):
    L = [app.getOptionBox(f"{i}") for i in range(5)]
    print(L)
    model.enregistre_reponse(image, L)
    img = ImageTk.PhotoImage(Image.open(
    model.lire_fichier()[0] + '/' + model.retrouve_image()))
    # app.addImageData("pic", ImageTk.PhotoImage(Image.open(
    #     model.lire_fichier()[0] + '/' + model.retrouve_image())), fmt="PhotoImage")


def interface(image, Q, L):
    app.setFont(size=20, family="Pumpkin Soup", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', sticky='NEW', stretch='COLUMN'):
        app.addLabel("en-tête", "outil de classification d'images")
        app.addImageData("pic", image, fmt="PhotoImage")
        app.setImageSize("pic", 100, 690)
    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
        app.addButton("Suivant", suivant(image))
    app.go()


model.init_annotation()
image = ImageTk.PhotoImage(Image.open(
    model.lire_fichier()[0] + '/' + model.retrouve_image()))
Q = model.lire_fichier()[1]
L = model.lire_fichier()[2]
interface(image, Q, L)
