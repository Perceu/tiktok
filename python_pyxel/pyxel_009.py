import pyxel
from random import randint


class Line:
    def __init__(self, y1, y2, x1, x2) -> None:
        self.y1=y1
        self.y2=y2
        self.velocity = 5
        self.x1=x1
        self.x2=x2
        self.color = randint(1,15)
        if self.color == 7:
            self.color = randint(8,15)


    def update(self):
        self.y1 += self.velocity
        self.y2 += self.velocity
    


class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False
        self.lines = []
        self.lines_2 = []
        self.lines.append(Line(0, -80, 0, self.width))
        self.lines_2.append(Line(-50, 0, 0, self.width))
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True
        
        if self.running:
            for idx, l in enumerate(self.lines):
                l.update()
                if l.y2 > self.height:
                    self.lines.pop(idx)

            for idx, l in enumerate(self.lines_2):
                l.update()
                if l.y2 > self.height:
                    self.lines_2.pop(idx)

            if self.lines[-1].y2 >= 0:
                l = self.lines[-1]
                distance = randint(-50,-25)
                self.lines.append(Line(0, distance, l.x2, l.x1))

            if self.lines_2[-1].y2 >= 0:
                l = self.lines_2[-1]
                distance = randint(-100,-50)
                self.lines_2.append(Line(0, distance, l.x2, l.x1))


    def draw(self):
        if self.running:
            if randint(0,1):
                pyxel.cls(0)
            for l in self.lines:
                pyxel.line(l.x1,l.y1, l.x2, l.y2, l.color)

            for l in self.lines_2:
                pyxel.line(l.x1,l.y1, l.x2, l.y2, 7)

App()