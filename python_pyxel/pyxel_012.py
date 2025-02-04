import pyxel
from random import randint, choice


class App:

    def __init__(self):
        self.width = 576
        self.height = 1024
        self.running = False
        self.position_y = 640
        self.position_x = 360
        self.multiple = 1
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True

    def draw(self):
        if self.running:
            pyxel.cls(0)
            size = 30
            pyxel.circ(self.position_x, self.position_y, size, 7)
            if self.position_y > 1200:
                self.multiple = -1
            elif self.position_y < 100:
                self.multiple = 1
            self.position_y += 5 * self.multiple

App()