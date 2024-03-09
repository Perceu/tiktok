import py5


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
        py5.no_fill()
        py5.stroke(255)
        size += 25
        py5.rect((py5.width / 2), (py5.height / 2) - 75, size, size)


py5.run_sketch()
