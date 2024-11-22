face = {
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
    def __init__(self,cube):
        self.cube=cube



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
        self.cube["Right"]=self.turn_right(self.cube["Right"])
    
        a1=[self.cube["Top"][i].copy() for i in range(len(self.cube["Top"]))]
        a2=[self.cube["Front"][i].copy() for i in range(len(self.cube["Front"]))]
        a3=[self.cube["Bottom"][i].copy() for i in range(len(self.cube["Bottom"]))]
        a4=[self.cube["Back"][i].copy() for i in range(len(self.cube["Back"]))]
    
        self.cube["Back"][0][2],self.cube["Back"][1][2],self.cube["Back"][2][2]=a1[0][2],a1[1][2],a1[2][2]
        self.cube["Top"][0][2],self.cube["Top"][1][2],self.cube["Top"][2][2]=a2[0][2],a2[1][2],a2[2][2]
        self.cube["Front"][0][2],self.cube["Front"][1][2],self.cube["Front"][2][2]=a3[0][2],a3[0][2],a3[0][2]
        self.cube["Bottom"][0][2],self.cube["Bottom"][1][2],self.cube["Bottom"][2][2]=a4[1][2],a4[0][2],a4[2][2]
        return 
    
    def R_(self): #vers le bas
        self.cube["Right"]=self.turn_left(self.cube["Right"])
        a1=[self.cube["Top"][i].copy() for i in range(len(self.cube["Top"]))]
        a2=[self.cube["Front"][i].copy() for i in range(len(self.cube["Front"]))]
        a3=[self.cube["Bottom"][i].copy() for i in range(len(self.cube["Bottom"]))]
        a4=[self.cube["Back"][i].copy() for i in range(len(self.cube["Back"]))]
        
        self.cube["Back"][0][2],self.cube["Back"][1][2],self.cube["Back"][2][2]=a3[0][2],a3[1][2],a3[2][2]
        self.cube["Top"][0][2],self.cube["Top"][1][2],self.cube["Top"][2][2]=a4[0][2],a4[1][2],a4[2][2]
        self.cube["Front"][0][2],self.cube["Front"][1][2],self.cube["Front"][2][2]=a1[0][2],a1[0][2],a1[0][2]
        self.cube["Bottom"][0][2],self.cube["Bottom"][1][2],self.cube["Bottom"][2][2]=a2[1][2],a2[0][2],a2[2][2]
        return 
    
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
    
    #face=turn_left(face)
base=base(face)
face=base.rotate_down()
for i in face:
    for e in face[i]:
        print(e)
    print("\n") 
