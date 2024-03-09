import py5
from random import randint
windown_size = width, height = 720, 1280
running = False
write_lines = False
y_location = 0
x_location = 0
positions = []
tuple_postion = None
def setup():
    global positions, y_location, x_location
    py5.size(*windown_size)
    py5.background(0)
    py5.color_mode(py5.HSB, 360, 100, 100)
    while y_location < 1300:
        positions.append((x_location, y_location, 20))
        x_location += 20 
        if x_location > py5.width+20:
            y_location += 20
            x_location = 0


def draw():
    global positions, running, tuple_postion
    
    if py5.is_key_pressed or running:
        running = True
        if tuple_postion:
            py5.no_fill()
            py5.stroke(0)
            py5.square(*tuple_postion)
        
        rand_hue = py5.random(360)
        lenght = len(positions)-1
        if lenght > 0:
            position = randint(0, lenght)
            tuple_postion = positions.pop(position)
        else:
            tuple_postion = positions.pop()
            running = False

        py5.fill(rand_hue, 80, 80)
        py5.stroke(rand_hue, 80, 80)
        py5.square(*tuple_postion)


py5.run_sketch()
