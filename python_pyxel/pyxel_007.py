import pyxel
from random import randint


class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False
        self.load = self.height
        self.scale = 10
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True

    def draw(self):
        if self.running:
            self.load -= self.scale
            if self.load < 0:
                self.scale = self.scale//2
                self.load = self.height
                if self.scale <= 0:
                    self.running = False

            for i in range(self.width):
                pyxel.pset(i, self.load, 7)

App()