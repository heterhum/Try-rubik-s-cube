from p5 import *

STEP=30
N=3
L0 = [(255, 255, 255), N+2, 1]  # Blanc
F0 = [(0, 255, 0), N+2, (N+1)+1]  # Vert
R0 = [(255, 255, 0), N+2, (N+1)*2+1]  # Jaune
B0 = [(0, 128, 255), N+2, (N+1)*3+1]  # Bleu
U0 = [(255, 0, 0), 1, N+1+1]  # Rouge
D0 = [(255, 165, 0), (N+1)*2+1, N+2]  # Orange
INFO_FACES = [L0, F0, R0, B0, U0, D0]


facet = {
    "Top": [
        ["🟩", "🟩", "🟩"], 
        ["🟩", "🟩", "🟩"], 
        ["🟩", "🟩", "🟩"]                                        
        ],
    "Bottom": [
        ["🟦", "🟦", "🟦"], 
        ["🟦", "🟦", "🟦"], 
        ["🟦", "🟦", "🟦"]
        ],
    "Left": [
        ["🟨", "🟨", "🟨"], 
        ["🟨", "🟨", "🟨"], 
        ["🟨", "🟨", "🟨"]
        ],
    "Right": [
        ["⬜", "⬜", "⬜"], 
        ["⬜", "⬜", "⬜"], 
        ["⬜", "⬜", "⬜"] 
        ],
    "Front": [
        ["🟥", "🟥", "🟥"], 
        ["🟥", "🟥", "🟥"], 
        ["🟥", "🟥", "🟥"]
        ]
        ,
    "Back": [
        ["🟧", "🟧", "🟧"], 
        ["🟧", "🟧", "🟧"], 
        ["🟧", "🟧", "🟧"]
        ]
}


def copie(cube):
    cube_copy={}
    e=[]
    for i in cube:
        cube_copy[i]=[]
        for e in cube[i]:
            cube_copy[i]+=[e.copy()]
    return cube_copy
            
class base:
    global INFO_FACES
    def __init__(self,cube):
        self.cube=cube
        self.L = [[L0[0] for _ in range(N)] for _ in range(N)]
        self.F = [[F0[0] for _ in range(N)] for _ in range(N)]
        self.R = [[R0[0] for _ in range(N)] for _ in range(N)]
        self.B = [[B0[0] for _ in range(N)] for _ in range(N)]
        self.U = [[U0[0] for _ in range(N)] for _ in range(N)]
        self.D = [[D0[0] for _ in range(N)] for _ in range(N)]


    def dessineFace(self,face, infoFace):
        for i in range(N):
            for j in range(N):
                fill(face[i][j])
                square((infoFace[2]+j) * STEP, (infoFace[1]+i) * STEP, STEP)

    def dessine(self):
        faceList = [self.L, self.F, self.R, self.B, self.U, self.D]
        for i in range(6):
            self.dessineFace(faceList[i], INFO_FACES[i])
#a "expliqué"
    def turn_right(self,face):
        c=list(zip(face[0],face[1],face[2]))
        d0=list(c[0])
        d0.reverse()
        d1=list(c[1])
        d1.reverse()
        d2=list(c[2])
        d2.reverse()
    
        face[0]=d0
        face[1]=d1
        face[2]=d2
        return face
    
    def turn_left(self,face):
        c=list(zip(face[0],face[1],face[2]))
        d0=list(c[2])
        d1=list(c[1])
        d2=list(c[0])
    
        face[0]=d0
        face[1]=d1
        face[2]=d2
        return face
    
    def R(self):   #vers le haut
        self.cube["Right"] = self.turn_right(self.cube["Right"])

        
        top_col = [self.cube["Top"][i][2] for i in range(3)]
        front_col = [self.cube["Front"][i][2] for i in range(3)]
        bottom_col = [self.cube["Bottom"][i][2] for i in range(3)]
        back_col = [self.cube["Back"][i][2] for i in range(3)]

        for i in range(3):
            self.cube["Top"][i][2] = front_col[i]
            self.cube["Front"][i][2] = bottom_col[i]
            self.cube["Bottom"][i][2] = back_col[2 - i]  
            self.cube["Back"][i][2] = top_col[2 - i]  
        return self.cube   

    
    def R_(self):  # vers le bas
        self.cube["Right"] = self.turn_left(self.cube["Right"])

        top_col = [self.cube["Top"][i][2] for i in range(3)]
        front_col = [self.cube["Front"][i][2] for i in range(3)]
        bottom_col = [self.cube["Bottom"][i][2] for i in range(3)]
        back_col = [self.cube["Back"][i][2] for i in range(3)]

        for i in range(3):
            self.cube["Top"][i][2] = back_col[2 - i]    
            self.cube["Front"][i][2] = top_col[i]
            self.cube["Bottom"][i][2] = front_col[i]
            self.cube["Back"][i][2] = bottom_col[2 - i]  
        return self.cube

    
    def rotate_right(self):
        cube_copy=copie(self.cube)

        self.cube["Front"]=cube_copy["Left"]
        self.cube["Right"]=cube_copy["Front"]
        self.cube["Left"]=cube_copy["Back"]
        self.cube["Back"]=cube_copy["Right"]
        
        self.cube["Top"]=self.turn_left(self.cube["Top"])
        self.cube["Bottom"]=self.turn_left(self.cube["Bottom"])
        return self.cube
    
    def rotate_left(self):
        cube_copy=copie(self.cube)

        self.cube["Front"]=cube_copy["Right"]
        self.cube["Right"]=cube_copy["Back"]
        self.cube["Left"]=cube_copy["Front"]
        self.cube["Back"]=cube_copy["Left"]
        
        self.cube["Top"]=self.turn_right(self.cube["Top"])
        self.cube["Bottom"]=self.turn_right(self.cube["Bottom"])
        return self.cube
    
    def rotate_up(self):
        cube_copy=copie(self.cube)

        self.cube["Top"]=cube_copy["Front"]
        self.cube["Front"]=cube_copy["Bottom"]
        self.cube["Bottom"]=cube_copy["Back"]
        self.cube["Back"]=cube_copy["Top"]
        
        self.cube["Right"]=self.turn_right(self.cube["Right"])
        self.cube["Left"]=self.turn_left(self.cube["Left"])
        return self.cube

    def rotate_down(self):
        cube_copy=copie(self.cube)

        self.cube["Top"]=cube_copy["Back"]
        self.cube["Front"]=cube_copy["Top"]
        self.cube["Bottom"]=cube_copy["Front"]
        self.cube["Back"]=cube_copy["Bottom"]
        
        self.cube["Right"]=self.turn_left(self.cube["Right"])
        self.cube["Left"]=self.turn_right(self.cube["Left"])
        return self.cube
    
    def rotatez_right(self):
        self.rotate_right()
        self.rotate_up()
        self.rotate_left()
        return self.cube 
    #10 fonction a faire mais flm
    #face=turn_left(face)
base=base(facet)
def setup():
    size(500,500)
    #background()

def draw():
    base.dessine()

run()
base=base(facet)
base.R()
base.rotatez_right()
for i in face:
    for e in face[i]:
        print(e)
    print("\n") 
