from p5 import *

STEP=100
N = 3

L0 = [(255, 255, 255), 0, N+1]  
F0 = [(0, 255, 0), N+1, N+1]  
R0 = [(255, 255, 0), (N+1)*2, N+1]  
B0 = [(0, 128, 255), (N+1)*3, N+1]  
U0 = [(255, 0, 0), N+1, 0]  
D0 = [(255, 165, 0), N+1, (N+1)*2]  
INFO_FACES = [L0, F0, R0, B0, U0, D0]
D = [[D0[0] for _ in range(N)]for _ in range(N)]#orange, bottom 
L = [[L0[0] for _ in range(N)]for _ in range(N)]#white, left
F = [[F0[0] for _ in range(N)]for _ in range(N)]#green, front
R = [[R0[0] for _ in range(N)]for _ in range(N)]#yellow, right
B = [[B0[0] for _ in range(N)]for _ in range(N)]#blue, back
U = [[U0[0] for _ in range(N)]for _ in range(N)]#red, top
INFO_FACES1 = [L, F, R, B, U, D]

def setup():
    size(600, 600)
    background(100)   

def draw():
    background(100)   
    rotateX(mouse_y/100)
    rotateY(mouse_x/100)
    
    for y in range(3):
        for x in range(3):
            translate(STEP*x,STEP*y)
            fill(D[y][x][0],D[y][x][1],D[y][x][2])
            plane(STEP,STEP)
            translate(-STEP*x,-STEP*y)
    rotateY(1)
    fill(0,0,0)
    plane(STEP,STEP)
run(mode="P3D",renderer="vispy")
help(rotate_y)