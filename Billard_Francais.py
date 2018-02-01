from tkinter import *
from random import *
import random
from math import *
import math
import turtle
import pygame
from pygame.locals import *
pygame.init()
##son = pygame.mixer.Sound("Boule_Choc.wav")
##son2 = pygame.mixer.Sound("Boule_rentre.wav")
##son3 = pygame.mixer.Sound("Boule_qui_revient.wav")
fen=Tk()
couleur=["white","red","green","blue","yellow","violet","orange","grey","brown","pink","purple","aqua","beige","chocolate","coral","crimson","cyan","fuchsia","gold","indigo","lawn green","lime","magenta","maroon","navy","olive","plum","salmon","silver","steel blue","tan"]
H=500
L=1000
aire= Canvas(fen,width=L,height=H,bg='grey')
aire.pack()

def CJ(O2,D):
	O1=0
	carré=aire.create_rectangle(O1,O2,O1+D,O2+D,fill="yellow")
	O1=950
	carré=aire.create_rectangle(O1,O2,O1+D,O2+D,fill="yellow")
	O1=475
	carré=aire.create_rectangle(O1,O2,O1+D,O2+D,fill="yellow")
def DN(Y,D):
	X=0
	disquenoir=aire.create_oval(X,Y,X+D,Y+D,fill="black",width=2)
	X=950
	disquenoir=aire.create_oval(X,Y,X+D,Y+D,fill="black",width=2)
	X=475
	disquenoir=aire.create_oval(X,Y,X+D,Y+D,fill="black",width=2)
def Bord(D,X1,X2):
	B=aire.create_polygon(X1,D,X2,D+20,X2,H-D-20,X1,H-D,fill="green",outline="black")
def Bord2(D,X1,X2):
	B=aire.create_polygon(D,X1,D+20,X2,L/2-(D/2)-20,X2,L/2-(D/2),X1,fill="green",outline="black")
	B=aire.create_polygon(L-D,X1,L-D-20,X2,L/2+(D/2)+20,X2,L/2+(D/2),X1,fill="green",outline="black")
def lignesblanches(x,y,x1,y1):
	ligne=aire.create_line(x,H/2,y,H/2,fill="white")
	ligne=aire.create_line(x,H/4,y,H/4,fill="white")
	ligne=aire.create_line(x,3*H/4,y,3*H/4,fill="white")
	ligne=aire.create_line(L/8,x1,L/8,y1,fill="white")
	ligne=aire.create_line(L/4,x1,L/4,y1,fill="white")
	ligne=aire.create_line(3*L/8,x1,3*L/8,y1,fill="white")
	ligne=aire.create_line(3*L/4,x1,3*L/4,y1,fill="white")
	ligne=aire.create_line(5*L/8,x1,5*L/8,y1,fill="white")
	ligne=aire.create_line(7*L/8,x1,7*L/8,y1,fill="white")

def terrain():
	D=50
	rectangle=aire.create_rectangle(20,20,L-20,H-20,fill="green",width=2)
	rectangle=aire.create_rectangle(30,30,L-30,H-30,fill="green",width=2)
	lignesblanches(5,15,5,15)
	lignesblanches(L-5,L-15,H-5,H-15)

terrain()
RAYON = 15
X = L*3/4
Y= H-100
Tour=0
##Y = H/2
# direction initiale aléatoire
vitesse = 10
##29
##1*1/5*
##angle = random.uniform(0,2*math.pi)
##def Clic(event):
##	global X,Y,vitesse
##	X1 = event.x
##	Y1 = event.y
##	angle=Al_Kashi(X,Y,X1,Y1,X,Y,X1,Y,X1,Y1,X1,Y)
##	DX = vitesse*math.cos(angle)
##	DY = vitesse*math.sin(angle)
##	deplacement(DX,DY)
angle=(70/100)*math.pi
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)
CA=2
k=0
choc=1
XR=L*(1/4)
YR=H/2
XJ=L/2
YJ=H-100
DYR=0
DXR=0
DXJ=0
DYJ=0
ChuteB=0
ChuteR=0
ChuteJ=0
D=50
activationblanc=0
activationrouge=0
conditionboucle=1
verification=[0,0,0,0]
Ok=1
Moment=0
def Al_Kashi(Xa1,Xa2,Ya1,Ya2,Xb1,Xb2,Yb1,Yb2,Xc1,Xc2,Yc1,Yc2):
    fA = sqrt((Xa1-Xa2)**2 + (Ya1-Ya2)**2)
    fB = sqrt((Xb1-Xb2)**2 + (Yb1-Yb2)**2)
    fC = sqrt((Xc1-Xc2)**2 + (Yc1-Yc2)**2)
    if fA==0:
    	fA=1/100
    if fB==0:
    	fB=1/100
    E=((fA**2) + (fB**2) - (fC**2)) / (2*fA*fB)
    E=(int(E*100))/100
    QS=acos(E)
    return QS
def deplacement():
    global X,Y,XJ,YJ,DX,DY,DXJ,DYJ,RAYON,L,H,couleur,x,y,d,CA,k,XR,YR,DXR,DYR,ChuteB,ChuteR,ChuteJ,D,Tour,activationblanc,activationrouge,conditionboucle,verification,Ok,Moment
    def collisiondubord(X,Y,DX,DY,option):
        if X+RAYON+DX > L-30:
            	X = 2*((L-30)-RAYON)-X
            	DX = -choc*DX
            	DY = choc*DY
        if X-RAYON+DX < 30:
            	X = 2*(RAYON+30)-X
            	DX = -choc*DX
            	DY = choc*DY

        if Y+RAYON+DY > H-30:
            	Y = 2*((H-30)-RAYON)-Y
            	DX = choc*DX
            	DY = -choc*DY
        if Y-RAYON+DY < 30:
            	Y = 2*(RAYON+30)-Y
            	DX = choc*DX
            	DY = -choc*DY
        if option==0:
        	return DX
        if option==1:
        	return DY
        if option==2:
        	return X
        if option==3:
        	return Y
    DX=collisiondubord(X,Y,DX,DY,0)
    DY=collisiondubord(X,Y,DX,DY,1)
    X=collisiondubord(X,Y,DX,DY,2)
    Y=collisiondubord(X,Y,DX,DY,3)
    DXR=collisiondubord(XR,YR,DXR,DYR,0)
    DYR=collisiondubord(XR,YR,DXR,DYR,1)
    XR=collisiondubord(XR,YR,DXR,DYR,2)
    YR=collisiondubord(XR,YR,DXR,DYR,3)
    DXJ=collisiondubord(XJ,YJ,DXJ,DYJ,0)
    DYJ=collisiondubord(XJ,YJ,DXJ,DYJ,1)
    XJ=collisiondubord(XJ,YJ,DXJ,DYJ,2)
    YJ=collisiondubord(XJ,YJ,DXJ,DYJ,3)


    ListeX=[X,XR,XJ]
    ListeY=[Y,YR,YJ]
    LDX=[DX,DXR,DXJ]
    LDY=[DY,DYR,DYJ]



    def collisionballe(X,Y,XR,YR,DX,DY,DXR,DYR,Tour,option):

    	if (DX!=0 or DY!=0) and (DYR!=0 or DXR!=0):
            angle1=Al_Kashi(X,X-DX,Y,Y-DY,X,X-DX,Y,Y,X-DX,X-DX,Y-DY,Y)
            angle2=Al_Kashi(XR,XR-DXR,YR,YR-DYR,XR,XR-DXR,YR,YR,XR-DXR,XR-DXR,YR-DYR,YR)
            v1=sqrt((DX**2)+((DY)**2))
            v2=sqrt((DXR**2)+((DYR)**2))
            angle1_2=atan((v2/v1)*(sin(angle2)/cos(angle1)))
            angle2_2=atan((v1/v2)*(sin(angle1)/cos(angle2)))
            v1_2=sqrt(((v2*sin(angle2))**2)+((v1*cos(angle1))**2))
            v2_2=sqrt(((v1*sin(angle1))**2)+((v2*cos(angle2))**2))
            DX=v1_2*cos(angle1_2)
            DY=v1_2*sin(angle1_2)
            DXR=v2_2*cos(angle2_2)
            DYR=v2_2*sin(angle2_2)
            if X-XR<0:
            	DX=-DX
            if Y-YR<0:
            	DY=-DY
            if XR-X<0:
            	DXR=-DXR
            if YR-Y<0:
            	DYR=-DYR
    	else:
            m=(DY/DX)
            p=Y-(m*X)
            c=-(((2*RAYON)**2)-(XR**2)-(YR**2)+(2*p*YR)-((p)**2))
            a=1+(m**2)
            b=2*((m*(p-YR))-XR)
            solution1=(((-b-(sqrt((b**2)-(4*c*a)))))/(2*a))
            solution2=(((-b+(sqrt((b**2)-(4*c*a)))))/(2*a))
            if DX<0:
            	X=solution2
            if DX>0:
            	X=solution1
            Y=(m*X)+p
            F=Al_Kashi(X,X+DX,Y,Y+DY,X,XR,Y,YR,XR,X+DX,YR,Y+DY)
            VitesseD=sqrt((DX**2) +(DY**2))
            angleV2=Al_Kashi(X,XR,Y,YR,X,XR,Y,Y,XR,XR,YR,Y)
            DXR=VitesseD*cos(F)*cos(angleV2)
            DYR=VitesseD*cos(F)*sin(angleV2)
            if XR-X<0:
            	DXR=-DXR
            if YR-Y<0:
            	DYR=-DYR
            DX=(DX-DXR)
            DY=(DY-DYR)
##        	son.play()
##        	son3.play()
    	if option==1:
        	return DXR
    	if option==2:
        	return DYR
    	if option==3:
        	return DX
    	if option==4:
        	return DY
    	if option==6:
        	return X
    	if option==7:
        	return Y
    	if option==8:
        	return XR
    	if option==9:
        	return YR
    verification=[0,0,0,0]
    for i in range (3):
    	Ok=1
    	if LDX[i]!=0 and LDY[i]!=0:
        	for k in range (3):
                    if ListeX[i]!=ListeX[k] and ListeY[i]!=ListeY[k]:
                    	condition=sqrt(((ListeX[i]-ListeX[k])**2)+((ListeY[i]-ListeY[k])**2))
                    	for e in range(i):
                            if condition==verification[e]:
                                Ok=0
                    	conditioncolision=(condition<=2*RAYON)
                    	if conditioncolision and Ok==1:
                            verification[i]=condition
                            if i==0 or k==0:
                                if i==0:
                                	option1=3
                                	option2=4
                                	option3=6
                                	option4=7
                                if k==0:
                                	option1=1
                                	option2=2
                                	option3=8
                                	option4=9
                            DX=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DY=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            X=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            Y=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                            if i==1 or k==1:
                            	if i==1:
                                	option1=3
                                	option2=4
                                	option3=6
                                	option4=7
                            	if k==1:
                                	option1=1
                                	option2=2
                                	option3=8
                                	option4=9
                            	DXR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            	DYR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            	XR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            	YR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                            if i==2 or k==2:
                            	if i==2:
                                	option1=3
                                	option2=4
                                	option3=6
                                	option4=7
                            	if k==2:
                                	option1=1
                                	option2=2
                                	option3=8
                                	option4=9
                            	DXJ=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            	DYJ=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            	XJ=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            	YJ=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)

##    	if option==8:
##        	return angleV2

####	angleV2=collisionballe(X,Y,XR,YR,DX,DY,DXR,DYR,Tour,8)
##	Tour=collisionballe(X,Y,XR,YR,DX,DY,DXR,DYR,Tour,9)

##	def frottement(DX,DY,angle,option):
##    	if DX>0:
##        	DX=DX-(5/100)*sqrt((cos(angle))**2)
##    	elif DX<0:
##        	DX=DX+(5/100)*sqrt((cos(angle))**2)
##    	if DY>0:
##        	DY=DY-(5/100)*sqrt((sin(angle))**2)
##    	elif DY<0:
##        	DY=DY+(5/100)*sqrt((sin(angle))**2)
##    	if option==0:
##        	return DX
##    	if option==1:
##        	return DY
##	DX=frottement(DX,DY,angle,0)
##	DY=frottement(DX,DY,angle,1)
##	DXR=frottement(DXR,DYR,angle,0)
##	DYR=frottement(DXR,DYR,angle,1)
    X = X+DX
    Y = Y+DY
    XR=XR+DXR
    YR=YR+DYR
    XJ=XJ+DXJ
    YJ=YJ+DYJ

##	Balleblancfall=((X<50 or L/2-25<X<L/2+25 or X>L-50) and (Y<50 or Y>450))
##	Ballerougefall=((XR<50 or L/2-25<XR<L/2+25 or XR>L-50) and (YR<50 or YR>450))


    aire.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    aire.coords(Ballerouge,XR-RAYON,YR-RAYON,XR+RAYON,YR+RAYON)
    aire.coords(Ballejaune,XJ-RAYON,YJ-RAYON,XJ+RAYON,YJ+RAYON)
    fen.after(20,deplacement)
##aire.bind('<B1-Motion>', Clic)
aire.pack(padx=5,pady=5)
Balle = aire.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,fill="white",width=1)
Ballerouge = aire.create_oval(XR-RAYON,YR-RAYON,XR+RAYON,YR+RAYON,fill="red",width=1)
Ballejaune = aire.create_oval(XJ-RAYON,YJ-RAYON,XJ+RAYON,YJ+RAYON,fill="yellow",width=1)
deplacement()
fen.mainloop()
