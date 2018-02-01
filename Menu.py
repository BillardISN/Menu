from tkinter import*
from Jeu_du_8 import*
from Francais import*
from Jeu_du_9 import*
import pygame

pygame.init()
son = pygame.mixer.Sound("This_Is_Tech_House.wav")
son.play()

def menu():
    global fen, fen2, fen3
    fen=Tk()
    aire=Canvas(fen,height=768, width=1802)
    mon_image = PhotoImage(file="menu.png", master=fen)
    logo= aire.create_image(901,384, image=mon_image)
    aire.image = mon_image
    aire.pack()
    Bouton1=Button(fen, text = "Billard Americain",command = Américain)
    Bouton1.pack()
    Bouton2=Button(fen, text= "Billard Français",command = Billard_Français)
    Bouton2.pack()
    Bouton3=Button(fen, text= "Règles",command = Règlement)
    Bouton3.pack()
    Bouton4=Button(fen, text= "Quitter", command= Quitter)
    Bouton4.pack()

def Règlement():
    fen=Tk()
    l=LabelFrame(fen, text="Règles",padx=20, pady=20)
    l.pack(fill="both",expand="yes")

    Label(l, text="Billard Français : \n\n Une partie de billard français se dispute à deux joueurs. L’un choisi la balle blanche et l’autre la balle jaune.\n Le but du jeu est de marquer le plus de points possible. \n Pour marquer un point, les joueurs  doivent toucher les deux autres billes en un tir.\n Tant que le joueur réussi à toucher les deux autres balles, il continu. Lorsqu’il manque le point, c’est son adversaire qui prend la main.").pack()

def Américain():
    fen.destroy()
    Billard_Americain()

def Billard_Français():
    fen.destroy()
    Francais()
    son.stop()

def Jeu8():
    fen.destroy()
    Jeu_du_8()
    son.stop()

def Jeu9():
    fen.destroy()
    Jeu_du_9()
    son.stop()

def Billard_Americain():
    global fen, fen2, fen3
    fen=Tk()
    aire=Canvas(fen,height=768, width=1802)
    mon_image = PhotoImage(file="menu.png", master=fen)
    logo= aire.create_image(901,384, image=mon_image)
    aire.image = mon_image
    aire.pack()
    Bouton1=Button(fen, text = "Jeu du 8",command= Jeu8)
    Bouton1.pack()
    Bouton2=Button(fen, text= "Jeu du 9",command= Jeu9)
    Bouton2.pack()
    Bouton3=Button(fen, text= "Quitter",command=Quitter)
    Bouton3.pack()
    Bouton4=Button(fen, text= "Retour",command=Retour)
    Bouton4.pack()

def Retour():
    fen.destroy()
    menu()
    son.stop()

def Quitter():
    fen.destroy()
    son.stop()
menu()
fen.mainloop()
