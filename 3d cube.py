#from p5 import *
#
#def setup():
#    size(600, 600)
#    background(100)   
#    lights()
#
#def draw():
#    background(100)
#    rotateX(mouse_y/100)
#    rotateY(mouse_x/100)
#    fill(255, 0, 0)
#    plane(100,100)
#    translate(100,100,0)
#    fill(0, 0, 250)
#    plane(100,100)
#    #fill(0,255,0)
#    #translate(-150,0,250)
#    #rotate_x(180)
#    #plane(300,300)
#
#run(mode="P3D",renderer="vispy")

from p5 import *
l=[[(0, 200, 0),(0, 100, 0),(0, 255, 0)],[(0, 255, 0),(0, 255, 0),(0, 255, 0)],[(0, 255, 0),(0, 255, 0),(0, 255, 0)]]
STEP=100
first=True

def setup():
    size(600, 600)
    background(100)   

def draw():
    global first
    background(100)   
    rotateX(mouse_y/1000)
    rotateY(mouse_x/1000)
    
    for y in range(3):
        for x in range(3):
            translate(STEP*x,STEP*y)
            fill(l[y][x][0],l[y][x][1],l[y][x][2])
            plane(STEP,STEP)
            translate(-(STEP*x),-(STEP*y))
    translate(0,STEP,STEP*3)
    plane(STEP,STEP)
run(mode="P3D",renderer="vispy")