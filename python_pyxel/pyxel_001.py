from turtle import width
import pyxel
from random import randint


class App:
    def __init__(self):
        self.width = 720
        self.height = 1280
        pyxel.init(self.width, self.height)
        self.running = False
        self.raio = 0
        self.color = 7

        self.position_x = int(self.width/2)
        self.position_y = int(self.height/2)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True
            
        if self.running:
            self.raio = (self.raio + 10) % pyxel.width
            if self.raio <= 10:
                self.position_x = randint(200,500)
                self.position_y = randint(200,1000)

    def draw(self):
        pyxel.cls(0)
        pyxel.circb(self.position_x, self.position_y, self.raio, self.color)

App()