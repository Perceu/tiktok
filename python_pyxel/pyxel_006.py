import pyxel
from random import randint


class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False

        self.colors = [
            0x00ff00,
            0x00e500,
            0x00cc00,
            0x00b200,
            0x009900,
            0x007f00,
            0x006600,
            0x004c00,
            0x003300,
            0xAA076B,
            0xFFFFFF,
        ][::-1]
        pyxel.init(self.width, self.height)
        pyxel.colors.from_list(self.colors)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True

    def draw(self):
        color = 1
        size = 10

        position_x = randint(10,self.width)
        position_y = randint(10,self.height)
        
        if self.running:
            pyxel.circ(position_x, position_y, size, color)

App()