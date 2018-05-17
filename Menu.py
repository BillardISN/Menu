from tkinter import*
from Billard import*
from Francais import*
import pygame
import ctypes
usr32 = ctypes.windll.user32

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("This_Is_Tech_House.wav")
pygame.mixer.music.play()

def menu():
    global fen, fen2, fen3
    fen=Tk()
    usr32 = ctypes.windll.user32
    aire=Canvas(fen,height=usr32.GetSystemMetrics(1)*0.8, width=usr32.GetSystemMetrics(0)*0.8)
    mon_image = PhotoImage(file="menu.png", master=fen)
    logo= aire.create_image((usr32.GetSystemMetrics(0)*0.8)*0.5,(usr32.GetSystemMetrics(1)*0.8)*0.5, image=mon_image)
    aire.image = mon_image
    Bouton4=Button(fen, text= "Quitter", command= Quitter)
    Bouton4.pack(side="bottom")
    Bouton3=Button(fen, text= "Règles",command = Règlement)
    Bouton3.pack(side="bottom")

    Bouton1=Button(fen, text = "Billard Français",command = Billard_Français)
    Bouton1.pack(side="bottom")
    Bouton2=Button(fen, text= "Billard Anglais",command = Jeu_Anglais )
    Bouton2.pack(side="bottom")

    fen.protocol("WM_DELETE_WINDOW",stop)
    aire.pack()
def stop():
    pygame.mixer.music.stop()
    fen.destroy()

def Règlement():
    fen=Tk()
    l=LabelFrame(fen, text="Règles",padx=20, pady=20)
    l.pack(fill="both",expand="yes")

    Label(l, text="Billard Français : \n\n Une partie de billard français se dispute à deux joueurs. L’un choisi la balle blanche et l’autre la balle jaune.\n Le but du jeu est de marquer le plus de points possible. \n Pour marquer un point, les joueurs  doivent toucher les deux autres billes en un tir.\n Tant que le joueur réussi à toucher les deux autres balles, il continu. Lorsqu’il manque le point, c’est son adversaire qui prend la main.").pack()

def Billard_Français():
    fen.destroy()
    Français()

def Jeu_Anglais():
    fen.destroy()
    Anglais()

def Retour():
    fen.destroy()
    menu()

def Quitter():
    fen.destroy()
    pygame.mixer.music.stop()

menu()
fen.mainloop()
