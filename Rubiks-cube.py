m=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]

t=[]

t.append([m[0][2],m[1][2],m[2][2]])

t.append([m[0][1],m[1][1],m[2][1]])

t.append([m[0][0],m[1][0],m[2][0]])


for i in m:
    print(i)
print("SPACE")

print(i for i in t)

top=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]
front=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]
bottom=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]
back=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]
left=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]
right=[
    ["A","Z","E"],
    ["R","T","Y"],
    ["U","I","O"]
]

import numpy as np
import matplotlib.pyplot as plt

cercle10 = plt.Circle((10,0),radius=10 , color='g', fill=False)
cercle11 = plt.Circle((10,0),radius=12 , color='g', fill=False)
cercle12 = plt.Circle((10,0),radius=14 , color='g', fill=False)

cercle20 = plt.Circle((22,0),radius=10 , color='y', fill=False)
cercle21 = plt.Circle((22,0),radius=12 , color='y', fill=False)
cercle22 = plt.Circle((22,0),radius=14 , color='y', fill=False)

cercle30 = plt.Circle((16,6*np.sqrt(3)),radius=10 , color='b', fill=False)
cercle31 = plt.Circle((16,6*np.sqrt(3)),radius=12 , color='b', fill=False)
cercle32 = plt.Circle((16,6*np.sqrt(3)),radius=14 , color='b', fill=False)

ax=plt.gca()
ax.add_patch(cercle10)
ax.add_patch(cercle11)
ax.add_patch(cercle12)

ax.add_patch(cercle20)
ax.add_patch(cercle21)
ax.add_patch(cercle22)

ax.add_patch(cercle30)
ax.add_patch(cercle31)
ax.add_patch(cercle32)


plt.axis('scaled')

# Affichage

plt.show()  

face = {
    "Top": [
        ["⬜", "⬜", "⬜"], 
        ["⬜", "⬜", "⬜"], 
        ["⬜", "⬜", "⬜"]
        ],
    "Bottom": [
        ["🟨", "🟨", "🟨"], 
        ["🟨", "🟨", "🟨"], 
        ["🟨", "🟨", "🟨"]
        ],
    "Left": [
        ["🟩", "🟩", "🟩"], 
        ["🟩", "🟩", "🟩"], 
        ["🟩", "🟩", "🟩"]
        ],
    "Right": [
        ["🟦", "🟦", "🟦"], 
        ["🟦", "🟦", "🟦"], 
        ["🟦", "🟦", "🟦"]
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

def turn1(dico):
    z=dico.copy()
    z["Top"][0][2],z["Top"][1][2],z["Top"][2][2]= dico["Front"][0][2],dico["Front"][1][2],dico["Front"][2][2]
    z["Back"][0][2],z["Back"][1][2],z["Back"][2][2]=dico["Top"][0][2],dico["Top"][1][2],dico["Top"][2][2]
    z["Bottom"][0][2],z["Bottom"][1][2],z["Bottom"][2][2]=dico["Back"][0][2],dico["Back"][1][2],dico["Back"][2][2]
    z["Front"][0][2],z["Front"][1][2],z["Front"][2][2]=dico["Bottom"][0][2],dico["Bottom"][1][2],dico["Bottom"][2][2]

    z["Right"][0][0]=dico["Right"][2][0]
    z["Right"][0][1]=dico["Right"][1][0]
    z["Right"][0][2]=dico["Right"][0][0]
    z["Right"][1][2]=dico["Right"][0][1]
    z["Right"][2][2]=dico["Right"][2][2]
    z["Right"][2][1]=dico["Right"][1][2]
    z["Right"][2][0]=dico["Right"][2][2]
    z["Right"][1][0]=dico["Right"][2][1]

    return z
dico=turn1(face)

def move_up(dico):
    z=dico.copy()
    z["Top"]=dico["Front"]

print(dico)