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

def move_up(dico):
    z=dico.copy()
    z["Top"]=dico["Front"]



#face=[["b","b","b"],["j","o","o"],["j","o","o"]]

#a "expliqué"
def turn_right(face):
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

def turn_left(face):
    c=list(zip(face[0],face[1],face[2]))
    d0=list(c[2])
    d1=list(c[1])
    d2=list(c[0])

    face[0]=d0
    face[1]=d1
    face[2]=d2
    return face

def R(cube):   #vers le haut
    cube["Right"]=turn_right(cube["Right"])

    a1=[cube["Top"][i].copy() for i in range(len(cube["Top"]))]
    a2=[cube["Front"][i].copy() for i in range(len(cube["Front"]))]
    a3=[cube["Bottom"][i].copy() for i in range(len(cube["Bottom"]))]
    a4=[cube["Back"][i].copy() for i in range(len(cube["Back"]))]

    cube["Back"][0][2],cube["Back"][1][2],cube["Back"][2][2]=a1[0][2],a1[1][2],a1[2][2]
    cube["Top"][0][2],cube["Top"][1][2],cube["Top"][2][2]=a2[0][2],a2[1][2],a2[2][2]
    cube["Front"][0][2],cube["Front"][1][2],cube["Front"][2][2]=a3[0][2],a3[0][2],a3[0][2]
    cube["Bottom"][0][2],cube["Bottom"][1][2],cube["Bottom"][2][2]=a4[1][2],a4[0][2],a4[2][2]
    return cube

def R_(cube): #vers le bas

    return

#face=turn_left(face)

dace=R(face)
for i in face:
    for e in face[i]:
        print(e)
    print("\n")
