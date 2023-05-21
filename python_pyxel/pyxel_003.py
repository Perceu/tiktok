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
        color = randint(0,15)
        border = randint(0,15)

        size = randint(3,30)
        size_2 = randint(10,100)

        position_x = randint(10,self.width)
        position_y = randint(10,self.height)
        
        if self.running:
            pyxel.circ(position_x, position_y, size, color)
            pyxel.circb(position_x, position_y, size_2, border)

App()