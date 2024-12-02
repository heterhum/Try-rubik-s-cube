from p5 import *

def setup():
    size(600, 600)
    background(100)   
    lights()

def draw():
    background(100)
    rotateX(mouse_y/100)
    rotateY(mouse_x/100)
    fill(255, 0, 0)
    plane(100,100)
    translate(100,100,0)
    fill(0, 0, 250)
    plane(100,100)
    #fill(0,255,0)
    #translate(-150,0,250)
    #rotate_x(180)
    #plane(300,300)

run(mode="P3D",renderer="vispy")