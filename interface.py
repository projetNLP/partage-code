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
    
def precedent():
    Q, L = model.lire_annote_image(image)
    app.stop()
    #la ligne suivante à modifier
    interface(image_resize, Q, L)

def interface(image_resize, Q, L):
    app.setFont(size=14, family="Verdana", underline=False, slant="roman")

    with app.frame("LEFT", row=0, column=0, bg='white', fg='black'):
        app.addLabel("en-tête", "outil de classification d'images")
        app.setLabelBg("en-tête", "DarkCyan")
        app.setLabelHeight("en-tête", 1)
        app.addImageData("pic", image_resize, fmt="PhotoImage")
        app.addButton("precedent", precedent)
        app.setButtonBg("precedent", "firebrick")
        app.setButtonWidth("precedent", 5)
        app.setButtonHeight("precedent", 1)

    with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
        for x in range(len(Q)):
            app.label(Q[x], bg='white')
            app.addLabelOptionBox(str(x), ["- select -"]+L[x])
            app.setLabelBg(Q[x], "bisque")

        app.addButton("suivant", suivant)
        app.setButtonFg("suivant", "white")
        app.setButtonBg("suivant", "limegreen")
        app.setButtonWidth("suivant", 5)
        app.setButtonHeight("suivant", 1)

    app.go()

model.init_annotation() # n'utiliser cette ligne que pour la première fois d'annotation pour un répertoire d'images
image = Image.open(model.lire_fichier()[0] + '/' + model.retrouve_image())
image_resize = ImageTk.PhotoImage(image.resize((600, 600)))
interface(image_resize, Q, L)
