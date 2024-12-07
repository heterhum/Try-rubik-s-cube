import pygame
import random as rd
import time 
pygame.init()

N=3
STEP=50
WIDTH=N*STEP*4+3*STEP
HEIGHT=N*STEP*3+2*STEP
firstt=True

screen = pygame.display.set_mode((WIDTH, HEIGHT))

L0 = [(255, 255, 255), 0, N+1]  
F0 = [(0, 255, 0), N+1, N+1]  
R0 = [(255, 255, 0), (N+1)*2, N+1]  
B0 = [(0, 128, 255), (N+1)*3, N+1]  
U0 = [(255, 0, 0), N+1, 0]  
D0 = [(255, 165, 0), N+1, (N+1)*2]  
INFO_FACES = [L0, F0, R0, B0, U0, D0]

def dessin_face(face,l): #dessiné une face en fonction des parametre donnée
    for i in range(N): #je commence par le cube en bas a gauche et finie paren haut a droite
        for e in range(N):
            x = (l[1] + i) * STEP
            y = (l[2] + e) * STEP
            pygame.draw.rect(screen,face[e][i],pygame.Rect(x, y, STEP, STEP))

    for i in range(N): 
        for e in range(N):
            x = (l[1] + i) * STEP
            y = (l[2] + e) * STEP
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(x, y, STEP, STEP),width=1)
def dessin():
    for i,l in zip(cube.INFO_FACES1,INFO_FACES): #lie la liste avec leur info
        dessin_face(i,l)

class cube():
    def __init__(self):
        self.D = [[D0[0] for _ in range(N)]for _ in range(N)]#orange, bottom 
        self.L = [[L0[0] for _ in range(N)]for _ in range(N)]#white, left
        self.F = [[F0[0] for _ in range(N)]for _ in range(N)]#green, front
        self.R = [[R0[0] for _ in range(N)]for _ in range(N)]#yellow, right
        self.B = [[B0[0] for _ in range(N)]for _ in range(N)]#blue, back
        self.U = [[U0[0] for _ in range(N)]for _ in range(N)]#red, top
        self.INFO_FACES1 = [self.L, self.F, self.R, self.B, self.U, self.D]
        self.rotatelist=["a","o","z","i","e","u","r","s","t","q","y","p","j","k","m","l","d","g","h","f"]

    def majface(self):
        self.INFO_FACES1=[self.L, self.F, self.R, self.B, self.U, self.D] #mes a jour toute les face utile sinon bug

    def rotationhor(self,face): #rotation matrice 90°
        return list(zip(*face[::-1]))
    def rotationantihor(self,face): #rotation matrice -90°
        return list(zip(*face))[::-1] #*face = toute les sous liste de la liste équivalent a : zip(face [0],face[1] ect ...)
                                      #le list() transforme les tuple en liste pour les manipulé
                                      #[::-1] méthode pour inversé chaque liste de la grande liste
    def rotateright(self): #rotation vers la droite, changement de POV
        self.U,self.R,self.D,self.L=list(zip(*self.L[::-1])),list(zip(*self.U[::-1])),list(zip(*self.R[::-1])),list(zip(*self.D[::-1]))
        self.F=self.rotationhor(self.F)
        self.B=self.rotationantihor(self.B)
        self.majface()
    def rotateleft(self): #changement de POV
        self.U,self.R,self.D,self.L=list(zip(*self.R))[::-1],list(zip(*self.D))[::-1],list(zip(*self.L))[::-1],list(zip(*self.U))[::-1]
        self.F=self.rotationantihor(self.F)
        self.B=self.rotationhor(self.B)
        self.majface()

    def Frotateright(self):#changement de POV
        self.F,self.R,self.B,self.L=self.L,self.F,self.R,self.B
        self.D=self.rotationhor(self.D)
        self.U=self.rotationantihor(self.U)
        self.majface()
    def Frotateleft(self):#changement de POV
        self.F,self.R,self.B,self.L=self.R,self.B,self.L,self.F
        self.U=self.rotationhor(self.U)
        self.D=self.rotationantihor(self.D)
        self.majface()

    def Mrotatetop(self):#changement de POV
        self.F,self.U,self.B,self.D=self.D,self.F,self.U[::-1],self.B[::-1]
        self.R=self.rotationhor(self.R)
        self.L=self.rotationantihor(self.L)
        self.majface()
    def Mrotatedown(self):#changement de POV
        self.Mrotatetop()
        self.Mrotatetop()
        self.Mrotatetop()

    def Dcube(self): #tour du crant en haut
        self.F[-1],self.R[-1],self.B[-1],self.L[-1]=self.L[-1],self.F[-1],self.R[-1],self.B[-1] #vient simplement remplacé chaque lst par une autre, comme sa évite d'avoir a faire des .copy()
        self.D=self.rotationhor(self.D) #la face d'en haut tourne dans un sens horraire donc j'apllique la fonction crée plus haut
        self.majface() #je mais a jour les face afin que toute les def est accès au meme valeurs
    def Dicube(self): #c'est la rotation de celle au dessus mais dans l'autre sens, si on tourne trois fois dans un sens c'est comme le tourné 1 fois dans l'autre
        self.Dcube()
        self.Dcube()
        self.Dcube()
    #def de toute les fonctions de rotation
    def Mcube(self):
        if N<=2: return
        n=input("emplacement ? : ")
        if not isinstance(n,int): n=1
        elif n<=0 or n>=N: n=1
        self.F[n],self.R[n],self.B[n],self.L[n]=self.L[n],self.F[n],self.R[n],self.B[n] #j'ai remplacé les 1 par n et monde code a été copatible avec toute les tailles de cubes
        self.majface()
    def Mcubespe(self):
        n=rd.randint(1, N-1)
        self.F[n],self.R[n],self.B[n],self.L[n]=self.L[n],self.F[n],self.R[n],self.B[n] #j'ai remplacé les 1 par n et monde code a été copatible avec toute les tailles de cubes
        self.majface()
    def Micube(self):
        self.Mcube()
        self.Mcube()
        self.Mcube()
    def Micubespe(self):
        self.Mcubespe()
        self.Mcubespe()
        self.Mcubespe()

    def Ucube(self):
        self.F[0],self.R[0],self.B[0],self.L[0]=self.L[0],self.F[0],self.R[0],self.B[0]
        self.U=self.rotationantihor(self.U)
        self.majface()
    def Uicube(self):
        self.Ucube()
        self.Ucube()
        self.Ucube()
    #flemme de les codé a la main du coup j'ai juste combiné des mouvements déja codé
    def Rcube(self):
        self.rotateright()
        self.Dcube()
        self.rotateleft()
        self.majface()
    def Ricube(self):
        self.Rcube()
        self.Rcube()
        self.Rcube()

    def Ecube(self):
        self.rotateright()
        self.Mcube()
        self.rotateleft()
        self.majface()
    def Ecubespe(self):
        self.rotateright()
        self.Mcubespe()
        self.rotateleft()
        self.majface()
    def Eicube(self):
        self.Ecube()
        self.Ecube()
        self.Ecube()
    def Eicubespe(self):
        self.Ecubespe()
        self.Ecubespe()
        self.Ecubespe()

    def Lcube(self):
        self.rotateright()
        self.Ucube()
        self.rotateleft()
        self.majface()
    def Licube(self):
        self.Lcube()
        self.Lcube()
        self.Lcube()

    def Ycube(self):
        self.Frotateright()
        self.Rcube()
        self.Frotateleft()
        self.majface()
    def Yicube(self):
        self.Frotateright()
        self.Ricube()
        self.Frotateleft()
        self.majface()
    def shuffle(self):
        l=""
        for _ in range(30):
            l+=rd.choice(self.rotatelist) # liste contenant les lettre
        
        for i in l:
            match i: # match associe les lettres a une fonction
                case pygame.K_a: cube.Lcube()
                case pygame.K_o: cube.Licube()
                case pygame.K_z: cube.Ecubespe()
                case pygame.K_i: cube.Eicubespe()
                case pygame.K_e: cube.Rcube()
                case pygame.K_u: cube.Ricube()
                case pygame.K_r: cube.Ucube()
                case pygame.K_s: cube.Uicube()
                case pygame.K_t: cube.Mcubespe()
                case pygame.K_q: cube.Micubespe()
                case pygame.K_y: cube.Dcube()
                case pygame.K_p: cube.Dicube()
                case pygame.K_j: cube.Ycube()
                case pygame.K_k: cube.Yicube()
                case pygame.K_m: cube.rotateleft()
                case pygame.K_l: cube.rotateright()
                case pygame.K_d: cube.Frotateright()
                case pygame.K_g: cube.Frotateleft()
                case pygame.K_h: cube.Mrotatetop()
                case pygame.K_f: cube.Mrotatedown()

cube=cube()

running = True
animation=0
while running:
    screen.fill((255, 255, 255))
    if animation<2000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        i=rd.choice(cube.rotatelist)
        match i: # match associe les lettres a une fonction
            case "a": cube.Lcube()
            case "o": cube.Licube()
            case "z": cube.Ecubespe()
            case "i": cube.Eicubespe()
            case "e": cube.Rcube()
            case "u": cube.Ricube()
            case "r": cube.Ucube()
            case "s": cube.Uicube()
            case "t": cube.Mcubespe()
            case "q": cube.Micubespe()
            case "y": cube.Dcube()
            case "p": cube.Dicube()
            case "j": cube.Ycube()
            case "k": cube.Yicube()
            case "m": cube.rotateleft()
            case "l": cube.rotateright()
            case "d": cube.Frotateright()
            case "g": cube.Frotateleft()
            case "h": cube.Mrotatetop()
            case "f": cube.Mrotatedown()
        animation+=1
        pygame.time.wait(500)
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a: cube.Lcube()
                    case pygame.K_o: cube.Licube()
                    case pygame.K_z: cube.Ecube()
                    case pygame.K_i: cube.Eicube()
                    case pygame.K_e: cube.Rcube()
                    case pygame.K_u: cube.Ricube()
                    case pygame.K_r: cube.Ucube()
                    case pygame.K_s: cube.Uicube()
                    case pygame.K_t: cube.Mcube()
                    case pygame.K_q: cube.Micube()
                    case pygame.K_y: cube.Dcube()
                    case pygame.K_p: cube.Dicube()
                    case pygame.K_j: cube.Ycube()
                    case pygame.K_k: cube.Yicube()
                    case pygame.K_m: cube.rotateleft()
                    case pygame.K_l: cube.rotateright()
                    case pygame.K_d: cube.Frotateright()
                    case pygame.K_g: cube.Frotateleft()
                    case pygame.K_h: cube.Mrotatetop()
                    case pygame.K_f: cube.Mrotatedown()
                    case pygame.K_n: cube.shuffle()
        if event.type == pygame.QUIT:
            running=False
    dessin()
    pygame.display.update()
quit()