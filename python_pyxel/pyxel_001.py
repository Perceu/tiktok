from turtle import width
import pyxel
from random import randint
class App:
    def __init__(self):
        width, height = 720, 1280
        pyxel.init(width, height)
        self.raio = 10
        self.color = 1

        self.position_x = int(width/2)
        self.position_y = int(height/2)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        

        self.raio = (self.raio + 10) % pyxel.width

        if self.raio <= 10:
            self.position_x = randint(200,500)
            self.position_y = randint(200,1000)

        self.color = (self.color + 1) % 15

    def draw(self):
        pyxel.cls(0)
        pyxel.circb(self.position_x, self.position_y, self.raio, self.color)

App()