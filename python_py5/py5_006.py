import py5
import random
windown_size = width, height = 720, 1280
running = False
circles = []

class Circle():
    def __init__(self, x, y, d) -> None:
        self.original_y = y
        self.y = y
        self.x = x
        self.d = d

    def draw(self):
        py5.circle(self.x, self.y, self.d)
    
    def update(self):
        self.y -= random.randint(1,6)
        self.x -= random.randint(-3,3)
        if (self.y + self.d) < 0:
            self.y = self.original_y


def setup():
    py5.size(*windown_size)
    py5.rect_mode(py5.CENTER)
    py5.fill(200,200,255, 95)
    py5.no_stroke()
    py5.background(0)
    for _ in range(1000):
        w = random.randint(5,py5.width-5)
        d = random.randint(10,30)
        c = Circle(w, random.randint(1280,2560), d)
        circles.append(c)


def draw():
    global running
    py5.background(0)
    if py5.is_key_pressed or running:
        running = True
        py5.background(0)
        for c in circles:
            c.update()
            c.draw()


py5.run_sketch()
