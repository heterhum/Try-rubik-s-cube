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
    plane(200,200)
    plane(300,300)

run(mode="P3D",renderer="vispy")