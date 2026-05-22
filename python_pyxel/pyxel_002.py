import pyxel
from random import randint


class App:

    def __init__(self):
        self.width = 576
        self.height = 1024
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
            size = randint(10,50)
            size_2 = randint(10,50)
            position_x = randint(0,self.width)
            position_y = randint(0,self.height)
            pyxel.rect(position_x, position_y, size, size, color)
            pyxel.rectb(position_x, position_y, size_2, size_2, 7)

App()