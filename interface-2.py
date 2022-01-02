from appJar import gui 
from tkinter import Toplevel
from tkinter.constants import TOP, UNDERLINE
from tkinter.font import families
from appJar import gui

from PIL import Image, ImageTk 
image = ImageTk.PhotoImage(Image.open("C:/Users/Omar/Downloads/a.jpg"))

def interface(image,Q,L):

        app=gui("interface","1000x700")
        app.setFont(size=20,family="Pumpkin Soup", underline=False,slant="roman")

        with app.frame("LEFT", row=0, column=0, bg='white', sticky='NEW', stretch='COLUMN'):
                app.addLabel("en-tête","outil de classification d'images")
                app.addImageData("pic", image, fmt="PhotoImage")
                app.setImageSize("pic",100,690)
                app.label("Retour", bg='red')
                app.setSize("Fullscreen")
        with app.frame("RIGHT", row=0, column=1, bg='white', fg='black'):
                for x in range(len(Q)):
                        app.label(Q[x], bg='white')
                        app.addLabelOptionBox(str(x), ["- select -"]+L[x])
                        app.label("Suivant", bg='Green')   
        app.go()





Q=["Question 1","Question 2","Question 3","Question 4","Question 5"]
L=[["oui","non"],["Lapin","chat"],["rouge","noir","jaune"],["oui","non"],["oui","non"]]               
interface(image,Q,L)

