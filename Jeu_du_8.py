from tkinter import *
from random import *
import random
from math import *
import math
import turtle
import pygame
pygame.init()
##son = pygame.mixer.Sound("Boule_Choc.wav")
##son2 = pygame.mixer.Sound("Boule_rentre.wav")
##son3 = pygame.mixer.Sound("Boule_qui_revient.wav")
fen=Tk()
couleur=["white","red","green","blue","yellow","violet","orange","grey","brown","pink","purple","aqua","beige","chocolate","coral","crimson","cyan","fuchsia","gold","indigo","lawn green","lime","magenta","maroon","navy","olive","plum","salmon","silver","steel blue","tan"]
H=500
L=1000
aire= Canvas(fen,width=L,height=H,bg='brown')
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
def terrain():
	D=50
	CJ(0,D)
	CJ(450,D)
	rectangle=aire.create_rectangle(20,20,L-20,H-20,fill="green",width=2)
	DN(0,D)
	DN(450,D)
	ligne=aire.create_line(L*(3/4),20,L*(3/4),H-20,fill="white")
	ligne2=aire.create_oval(L*(3/4)-100,(H/2)-100,(L*(3/4))+100,(H/2)+100,outline="white")
	rectangle2=aire.create_rectangle(L*(3/4)-100,(H/2)-100,L*(3/4)-1,(H/2)+100,outline="green",fill="green")
	Bord(D,20,30)
	Bord(D,L-20,L-30)
	Bord2(D,20,30)
	Bord2(D,H-20,H-30)
terrain()
RAYON = 15
X = L*3/4
##Y= H-35
Tour=0
Y = H/2
# direction initiale aléatoire
vitesse = 10
##1*1/5*
##angle = random.uniform(0,2*math.pi)
angle=(101/100)*math.pi
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)
##DX=0
##DY=0
CA=2
k=0
choc=0.85
XJ=L/3
YJ=H/2
XR=XJ-(sqrt(3)*RAYON)-1
YR=YJ+RAYON+1
XB=XJ-(sqrt(3)*RAYON)-1
YB=YJ-RAYON-1
XV=XB-(sqrt(3)*RAYON)-1
YV=YB-RAYON-1
XBR=XB-(sqrt(3)*RAYON)-1
YBR=YB+RAYON
XVI=XR-(sqrt(3)*RAYON)-1
YVI=YR+RAYON+1
XO=XV-(sqrt(3)*RAYON)-1
YO=YV-RAYON-0.5
XN=XV-(sqrt(3)*RAYON)-1
YN=YV+RAYON-0.25
XVF=XVI-(sqrt(3)*RAYON)-1
YVF=YVI-RAYON+0.25
XBC=XVI-(sqrt(3)*RAYON)-1
YBC=YVI+RAYON+0.5
DYR=0
DXR=0
DXJ=0
DYJ=0
DXB=0
DYB=0
DXV=0
DYV=0
DXO=0
DYO=0
DXBR=0
DYBR=0
DXVI=0
DYVI=0
DXN=0
DYN=0
DXVF=0
DYVF=0
DXBC=0
DYBC=0
ChuteB=0
ChuteR=0
ChuteJ=0
D=50
activationblanc=0
activationrouge=0
conditionboucle=1
Ok=1
Tourpremier=0
DYR=0
DXR=0
DXJ=0
DYJ=0
DXB=0
DYB=0
DXV=0
DYV=0
DXO=0
DYO=0
DXBR=0
DYBR=0
DXVI=0
DYVI=0
DXN=0
DYN=0
DXVF=0
DYVF=0
DXBC=0
DYBC=0
ChuteB=0
ChuteV=0
ChuteBR=0
ChuteVI=0
ChuteO=0
ChuteN=0
ChuteVF=0
ChuteBC=0

def deplacement():
    global X,Y,DX,DY,DYR,DXR,DXJ,DYJ,DXB,DYB,DXV,DYV,DXO,DYO,DXBR,DYBR,DXVI,DYVI,DXN,DYN,DXVF,DYVF,DXBC,DYBC,XJ,YJ,XB,YB,XV,YV,XBR,YBR,XVI,YVI,XO,YO,XN,YN,XVF,YVF,XBC,YBC,RAYON,L,H,couleur,x,y,d,CA,k,XR,YR,Tourpremier,ChuteB,ChuteR,ChuteJ,ChuteB,ChuteV,ChuteBR,ChuteVI,ChuteO,ChuteN,ChuteVF,ChuteBC,D,Tour,activationblanc,activationrouge,conditionboucle,Ok
    def collisiondubord(X,Y,DX,DY,option):
        if D<=Y<=H-D:
            if X+RAYON+DX > L-30:
                X = 2*((L-30)-RAYON)-X
                DX = -choc*DX
                DY = choc*DY
            if X-RAYON+DX < 30:
            	X = 2*(RAYON+30)-X
            	DX = -choc*DX
            	DY = choc*DY
        if D<=X<=(L/2)-25 or (L/2)+25<=X<=L-D:
        	# rebond en bas
            if Y+RAYON+DY > H-30:
            	Y = 2*((H-30)-RAYON)-Y
            	DX = choc*DX
            	DY = -choc*DY
        	# rebond en haut
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
    DXB=collisiondubord(XB,YB,DXB,DYB,0)
    DYB=collisiondubord(XB,YB,DXB,DYB,1)
    XB=collisiondubord(XB,YB,DXB,DYB,2)
    YB=collisiondubord(XB,YB,DXB,DYB,3)
    DXV=collisiondubord(XV,YV,DXV,DYV,0)
    DYV=collisiondubord(XV,YV,DXV,DYV,1)
    XV=collisiondubord(XV,YV,DXV,DYV,2)
    YV=collisiondubord(XV,YV,DXV,DYV,3)
    DXO=collisiondubord(XO,YO,DXO,DYO,0)
    DYO=collisiondubord(XO,YO,DXO,DYO,1)
    XO=collisiondubord(XO,YO,DXO,DYO,2)
    YO=collisiondubord(XO,YO,DXO,DYO,3)
    DXBR=collisiondubord(XBR,YBR,DXBR,DYBR,0)
    DYBR=collisiondubord(XBR,YBR,DXBR,DYBR,1)
    XBR=collisiondubord(XBR,YBR,DXBR,DYBR,2)
    YBR=collisiondubord(XBR,YBR,DXBR,DYBR,3)
    DXVI=collisiondubord(XVI,YVI,DXVI,DYVI,0)
    DYVI=collisiondubord(XVI,YVI,DXVI,DYVI,1)
    XVI=collisiondubord(XVI,YVI,DXVI,DYVI,2)
    YVI=collisiondubord(XVI,YVI,DXVI,DYVI,3)
    DXN=collisiondubord(XN,YN,DXN,DYN,0)
    DYN=collisiondubord(XN,YN,DXN,DYN,1)
    XN=collisiondubord(XN,YN,DXN,DYN,2)
    YN=collisiondubord(XN,YN,DXN,DYN,3)
    DXVF=collisiondubord(XVF,YVF,DXVF,DYVF,0)
    DYVF=collisiondubord(XVF,YVF,DXVF,DYVF,1)
    XVF=collisiondubord(XVF,YVF,DXVF,DYVF,2)
    YVF=collisiondubord(XVF,YVF,DXVF,DYVF,3)
    DXBC=collisiondubord(XBC,YBC,DXBC,DYBC,0)
    DYBC=collisiondubord(XBC,YBC,DXBC,DYBC,1)
    XBC=collisiondubord(XBC,YBC,DXBC,DYBC,2)
    YBC=collisiondubord(XBC,YBC,DXBC,DYBC,3)
    ListeX=[X,XR,XJ,XB,XV,XBR,XVI,XO,XN,XVF,XBC]
    ListeY=[Y,YR,YJ,YB,YV,YBR,YVI,YO,YN,YVF,YBC]
    LDX=[DX,DXR,DXJ,DXB,DXV,DXO,DXBR,DXVI,DXN,DXVF,DXBC]
    LDY=[DY,DYR,DYJ,DYB,DYV,DYO,DYBR,DYVI,DYN,DYVF,DYBC]

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
            Tour=0
##            son.play()
##            son3.play()
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

    verification=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (11):
        Ok=1
        if LDX[i]!=0 and LDY[i]!=0:
            for k in range (11):
                if ListeX[i]!=ListeX[k] and ListeY[i]!=ListeY[k]:
                    condition=sqrt(((ListeX[i]-ListeX[k])**2)+((ListeY[i]-ListeY[k])**2))
                    for e in range(i*k):
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
                        if i==3 or k==3:
                            if i==3:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==3:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXB=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYB=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XB=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YB=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==4 or k==4:
                            if i==4:
                                option1=3
                                option2=4
                                option3=6
                                option4=7
                            if k==4:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXV=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYV=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XV=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YV=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==5 or k==5:
                            if i==5:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==5:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXBR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYBR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XBR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YBR=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==6 or k==6:
                            if i==6:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==6:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXVI=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYVI=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XVI=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YVI=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==7 or k==7:
                            if i==7:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==7:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXO=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYO=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XO=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YO=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==8 or k==8:
                            if i==8:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==8:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXN=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYN=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XN=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YN=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==9 or k==9:
                            if i==9:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==9:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXVF=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYVF=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XVF=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YVF=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
                        if i==10 or k==10:
                            if i==10:
                            	option1=3
                            	option2=4
                            	option3=6
                            	option4=7
                            if k==10:
                            	option1=1
                            	option2=2
                            	option3=8
                            	option4=9
                            DXBC=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option1)
                            DYBC=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option2)
                            XBC=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option3)
                            YBC=collisionballe(ListeX[i],ListeY[i],ListeX[k],ListeY[k],LDX[i],LDY[i],LDX[k],LDY[k],Tour,option4)
##    	if option==8:
##        	return angleV2

####	angleV2=collisionballe(X,Y,XR,YR,DX,DY,DXR,DYR,Tour,8)


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
    XB = XB+DXB
    YB = YB+DYB
    XV = XV+DXV
    YV = YV+DYV
    XBR = XBR+DXBR
    YBR = YBR+DYBR
    XVI = XVI+DXVI
    YVI = YVI+DYVI
    XO = XO+DXO
    YO = YO+DYO
    XVF = XVF+DXVF
    YVF = YVF+DYVF
    XN = XN+DXN
    YN = YN+DYN
    XBC = XBC+DXBC
    YBC = YBC+DYBC

##	Balleblancfall=((X<50 or L/2-25<X<L/2+25 or X>L-50) and (Y<50 or Y>450))
##	Ballerougefall=((XR<50 or L/2-25<XR<L/2+25 or XR>L-50) and (YR<50 or YR>450))
    def Ballefall(DX,DY,X,Y,ChuteB,activationblanc,option):
    	Balleblancfall=((X<50 or L/2-25<X<L/2+25 or X>L-50) and (Y<50 or Y>450))
    	if Balleblancfall:
            DX=0
            DY=0
            if Y<50:
            	Y=25
            elif Y>450:
            	Y=475
            if X<50:
            	X=25
            elif L/2-25<X<L/2+25:
            	X=L/2
            elif X>L-50:
            	X=L-25
            ChuteB=ChuteB+1

    	if Balleblancfall and activationblanc==0:
    	##    	son2.play()
        	activationblanc=1
    	if option==0:
        	return DX
    	if option==1:
        	return DY
    	if option==2:
        	return X
    	if option==3:
        	return Y
    	if option==4:
        	return ChuteB
    DX=Ballefall(DX,DY,X,Y,ChuteB,activationblanc,0)
    DY=Ballefall(DX,DY,X,Y,ChuteB,activationblanc,1)
    X=Ballefall(DX,DY,X,Y,ChuteB,activationblanc,2)
    Y=Ballefall(DX,DY,X,Y,ChuteB,activationblanc,3)
    ChuteB=Ballefall(DX,DY,X,Y,ChuteB,activationblanc,4)
    DXR=Ballefall(DXR,DYR,XR,YR,ChuteR,activationblanc,0)
    DYR=Ballefall(DXR,DYR,XR,YR,ChuteR,activationblanc,1)
    XR=Ballefall(DXR,DYR,XR,YR,ChuteR,activationblanc,2)
    YR=Ballefall(DXR,DYR,XR,YR,ChuteR,activationblanc,3)
    ChuteR=Ballefall(DXR,DYR,XR,YR,ChuteR,activationblanc,4)
    DXJ=Ballefall(DXJ,DYJ,XJ,YJ,ChuteJ,activationblanc,0)
    DYJ=Ballefall(DXJ,DYJ,XJ,YJ,ChuteJ,activationblanc,1)
    XJ=Ballefall(DXJ,DYJ,XJ,YJ,ChuteJ,activationblanc,2)
    YJ=Ballefall(DXJ,DYJ,XJ,YJ,ChuteJ,activationblanc,3)
    ChuteJ=Ballefall(DXJ,DYJ,XJ,YJ,ChuteJ,activationblanc,4)
    if RAYON-1<=ChuteB<=RAYON+1:
                	aire.delete(Balle)
                	X=-100
                	Y=-100
    if RAYON-1<=ChuteR<=RAYON+1:
                	aire.delete(Ballerouge)
                	XR=-200
                	YR=-200
    if RAYON-1<=ChuteJ<=RAYON+1:
                	aire.delete(Ballejaune)
                	XJ=-300
                	YJ=-300
    aire.coords(Balle,X-RAYON+ChuteB,Y-RAYON+ChuteB,X+RAYON-ChuteB,Y+RAYON-ChuteB)
    aire.coords(Ballerouge,XR-RAYON+ChuteR,YR-RAYON+ChuteR,XR+RAYON-ChuteR,YR+RAYON-ChuteR)
    aire.coords(Ballejaune,XJ-RAYON+ChuteJ,YJ-RAYON+ChuteJ,XJ+RAYON-ChuteJ,YJ+RAYON-ChuteJ)
    aire.coords(Ballebleue,XB-RAYON+ChuteB,YB-RAYON+ChuteB,XB+RAYON-ChuteB,YB+RAYON-ChuteB)
    aire.coords(Ballevert,XV-RAYON+ChuteV,YV-RAYON+ChuteV,XV+RAYON-ChuteV,YV+RAYON-ChuteV)
    aire.coords(Ballebrun,XBR-RAYON+ChuteBR,YBR-RAYON+ChuteBR,XBR+RAYON-ChuteBR,YBR+RAYON-ChuteBR)
    aire.coords(Balleviolet,XVI-RAYON+ChuteVI,YVI-RAYON+ChuteVI,XVI+RAYON-ChuteVI,YVI+RAYON-ChuteVI)
    aire.coords(Balleorange,XO-RAYON+ChuteO,YO-RAYON+ChuteO,XO+RAYON-ChuteO,YO+RAYON-ChuteO)
    aire.coords(Ballenoir,XN-RAYON+ChuteN,YN-RAYON+ChuteN,XN+RAYON-ChuteN,YN+RAYON-ChuteN)
    aire.coords(Ballevertfoncé,XVF-RAYON+ChuteVF,YVF-RAYON+ChuteVF,XVF+RAYON-ChuteVF,YVF+RAYON-ChuteVF)
    aire.coords(Ballebleuclair,XBC-RAYON+ChuteBC,YBC-RAYON+ChuteBC,XBC+RAYON-ChuteBC,YBC+RAYON-ChuteBC)
    fen.after(30,deplacement)
aire.pack(padx=5,pady=5)
Balle = aire.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,fill="white",width=1)
Ballerouge = aire.create_oval(XR-RAYON,YR-RAYON,XR+RAYON,YR+RAYON,fill="red",width=1)
Ballejaune = aire.create_oval(XJ-RAYON,YJ-RAYON,XJ+RAYON,YJ+RAYON,fill="yellow",width=1)
Ballebleue = aire.create_oval(XB-RAYON,YB-RAYON,XB+RAYON,YB+RAYON,fill="blue",width=1)
Ballevert = aire.create_oval(XV-RAYON,YV-RAYON,XV+RAYON,YV+RAYON,fill="green",width=1)
Ballebrun = aire.create_oval(XBR-RAYON,YBR-RAYON,XBR+RAYON,YBR+RAYON,fill="brown",width=1)
Balleviolet = aire.create_oval(XVI-RAYON,YVI-RAYON,XVI+RAYON,YVI+RAYON,fill="purple",width=1)
Balleorange = aire.create_oval(XO-RAYON,YO-RAYON,XO+RAYON,YO+RAYON,fill="orange",width=1)
Ballenoir = aire.create_oval(XN-RAYON,YN-RAYON,XN+RAYON,YN+RAYON,fill="black",width=1)
Ballevertfoncé = aire.create_oval(XVF-RAYON,YVF-RAYON,XVF+RAYON,YVF+RAYON,fill="light green",width=1)
Ballebleuclair = aire.create_oval(XBC-RAYON,YBC-RAYON,XBC+RAYON,YBC+RAYON,fill="light blue",width=1)
deplacement()
fen.mainloop()
