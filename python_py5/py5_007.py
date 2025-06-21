from py5 import Sketch
import colorsys

windown_size = width, height = 480, 854

class MySquare():
    size = 0
    aumento = 5
    limit_size = 50
    delay = 0

    def __init__(self, x, y, velocidade, color, delay=0):
        self.x = x
        self.y = y
        self.aumento = velocidade
        self.delay = delay
        self.color = color

    def update(self):
        if self.delay > 0:
            self.delay -= 1
            return

        self.size += self.aumento
        if self.size > self.limit_size or self.size < 0:
            self.aumento *= -1

    def draw(self, sk: Sketch):
        sk.fill(*self.color)
        sk.rect(self.x, self.y, self.size, self.size)


class TestSketch(Sketch):
    space = 50
    quadrados = []
    hue_color = 0

    def draw_lines(self):
        for x in range(0, self.width, self.space):
            for y in range(0, self.height, self.space):
                if (self.space + x) < self.width:
                    self.line(x, y, x + self.space, y)
                if (self.space + y) < self.height:
                    self.line(x, y, x, y + self.space)

    def settings(self):
        self.size(*windown_size)

    def setup(self):
        self.rect_mode(self.CENTER)
        self.background(0)
        self.frame_rate(30)
        self.stroke(255)
        delay = 0

        for idx, y in enumerate(range(0, self.height, self.space)):
            self.hue_color = 0
            if (idx % 2 == 0):
                for x in range(0, self.width+50, self.space):
                    delay += 5
                    if (delay % 50 == 0):
                        delay = 0
                    self.hue_color += 0.3
                    color = colorsys.hsv_to_rgb(self.hue_color, 1, 1)
                    color = int(color[0]*255), int(color[1]*255), int(color[2]*255)
                    self.quadrados.append(
                        MySquare(x, y, 5, color, delay)
                    )
            else:
                for x in range(0, self.width+50, self.space):
                    delay += 8
                    if (delay % 80 == 0):
                        delay = 0
                    self.hue_color += 0.003
                    color = colorsys.hsv_to_rgb(self.hue_color, 1, 1)
                    color = int(color[0]*255), int(color[1]*255), int(color[2]*255)
                    self.quadrados.append(
                        MySquare(x, y, 5, color, delay)
                    )

    def draw(self):
        self.background(0)
        # self.draw_lines()
        for q in self.quadrados:
            q.update()
            q.draw(self)


test = TestSketch()
test.run_sketch()
