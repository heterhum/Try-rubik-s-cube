from p5 import *

STEP = 30 
N = 3  


L0 = [(255, 255, 255), 0, N+1]  
F0 = [(0, 255, 0), N+1, N+1]  
R0 = [(255, 255, 0), (N+1)*2, N+1]  
B0 = [(0, 128, 255), (N+1)*3, N+1]  
U0 = [(255, 0, 0), N+1, 0]  
D0 = [(255, 165, 0), N+1, (N+1)*2]  
INFO_FACES = [L0, F0, R0, B0, U0, D0]

def dessin_face(face,l):
    for i in range(N):
        for e in range(N):            
            x = (l[1] + i) * STEP
            y = (l[2] + e) * STEP
            fill(face[e][i][0],face[e][i][1],face[e][i][2])  
            square(x, y, STEP)
def dessin():
    for i,l in zip(cube.INFO_FACES1,INFO_FACES):
        dessin_face(i,l)

class cube():

    def __init__(self):
        
        self.D = [[D0[0] for _ in range(3)]for _ in range(3)]#orange, bottom 
        self.L = [[L0[0] for _ in range(3)]for _ in range(3)]#white, left
        self.F = [[F0[0] for _ in range(3)]for _ in range(3)]#green, front
        self.R = [[R0[0] for _ in range(3)]for _ in range(3)]#yellow, right
        self.B = [[B0[0] for _ in range(3)]for _ in range(3)]#blue, back
        self.U = [[U0[0] for _ in range(3)]for _ in range(3)]#red, top
        self.INFO_FACES1 = [self.L, self.F, self.R, self.B, self.U, self.D]

    def majface(self):
        self.INFO_FACES1=[self.L, self.F, self.R, self.B, self.U, self.D]

    def rotationhor(self,face):
        return list(zip(*face[::-1]))
    def rotationantihor(self,face):
        return list(zip(*face))[::-1]
    
    def rotateright(self):
        self.U,self.R,self.D,self.L=list(zip(*self.L[::-1])),list(zip(*self.U[::-1])),list(zip(*self.R[::-1])),list(zip(*self.D[::-1]))
        self.F=self.rotationhor(self.F)
        self.B=self.rotationantihor(self.B)
        self.majface()
    def rotateleft(self):
        self.U,self.R,self.D,self.L=list(zip(*self.R))[::-1],list(zip(*self.D))[::-1],list(zip(*self.L))[::-1],list(zip(*self.U))[::-1]
        self.F=self.rotationantihor(self.F)
        self.B=self.rotationhor(self.B)
        self.majface()

    def Frotateright(self):
        self.F,self.R,self.B,self.L=self.L,self.F,self.R,self.B
        self.D=self.rotationhor(self.D)
        self.U=self.rotationantihor(self.U)
        self.majface()
    def Frotateleft(self):
        self.F,self.R,self.B,self.L=self.R,self.B,self.L,self.F
        self.U=self.rotationhor(self.U)
        self.D=self.rotationantihor(self.D)
        self.majface()


    #TO DO, réglé cette fonction, testé pour voir le problème
    def Mrotatetop(self):
        self.F,self.U,self.B,self.D=self.D,self.F,self.U,self.B
        self.R=self.rotationhor(self.R)
        self.L=self.rotationantihor(self.L)
        self.majface()
    def Mrotatedown(self):
        self.Mrotatetop()
        self.Mrotatetop()
        self.Mrotatetop()

    def Dcube(self):
        self.F[2],self.R[2],self.B[2],self.L[2]=self.L[2],self.F[2],self.R[2],self.B[2]
        self.D=self.rotationhor(self.D)
        self.majface()
    def Dicube(self):
        self.Dcube()
        self.Dcube()
        self.Dcube()

    def Mcube(self):
        self.F[1],self.R[1],self.B[1],self.L[1]=self.L[1],self.F[1],self.R[1],self.B[1]
        self.majface()
    def Micube(self):
        self.Mcube()
        self.Mcube()
        self.Mcube()

    def Ucube(self):
        self.F[0],self.R[0],self.B[0],self.L[0]=self.L[0],self.F[0],self.R[0],self.B[0]
        self.U=self.rotationantihor(self.U)
        self.majface()
    def Uicube(self):
        self.Ucube()
        self.Ucube()
        self.Ucube()

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
    def Eicube(self):
        self.Ecube()
        self.Ecube()
        self.Ecube()

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

cube=cube()

def setup():
    size(500, 500)
    background(240)

def draw():
    dessin()

def key_pressed():
    match key:
        case "a": cube.Lcube()
        case "o": cube.Licube()
        case "z": cube.Ecube()
        case "i": cube.Eicube()
        case "e": cube.Rcube()
        case "u": cube.Ricube()
        case "r": cube.Ucube()
        case "s": cube.Uicube()
        case "t": cube.Mcube()
        case "q": cube.Micube()
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

run()