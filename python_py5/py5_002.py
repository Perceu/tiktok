import py5
import random 

windown_size = width, height = 720, 1280
running = False
size = 5


def setup():
    py5.size(*windown_size)
    py5.rect_mode(py5.CENTER)
    py5.fill(255)
    py5.background(0)


def draw():
    global size, running
    if py5.is_key_pressed or running:
        running = True
        for _ in range(2):
            x = random.randint(0, py5.width)
            y = random.randint(0, py5.height)
            size = random.randint(5, 100)
            py5.fill(random.randint(0, 255))
            py5.ellipse(x, y, size, size)


py5.run_sketch()
