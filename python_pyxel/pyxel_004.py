import pyxel
from random import randint


class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False

        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True

    def draw(self):
        if self.running:
            color = randint(0,15)
            border = 7

            x11 = randint(10, self.width)
            y11 = randint(10, self.height)

            x21 = x11+randint(80,200)
            y21 = y11-randint(10,110)

            x31 = x21-randint(10,100)
            y31 = y21+randint(10,90)

            x12 = x11+randint(10,100)
            y12 = y11+randint(20,220)

            x22 = x12+randint(10,100)
            y22 = y12-randint(20,220)

            x32 = x22+randint(10,100)
            y32 = y22+randint(20,220)

            pyxel.tri(x11, y11, x21, y21, x31, y31, color)
            pyxel.trib(x12, y12, x22, y22, x32, y32, border)

App()