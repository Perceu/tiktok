import pyxel
from random import randint, choice


class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False
        self.position_y = -30
        self.position_x = 0
        self.position_2_y = -30
        self.position_2_x = 0
        self.left = 0
        self.color = 7
        self.positions = list(range(40, self.width, 40))
        self.moviment = 1

        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True

    def write_snake(self, size, x, color):
            self.position_x = x
            self.position_y += 20
            self.position_2_y += 20

            if self.left:
                self.left = 0
                self.position_x = self.position_x-((size/2)*self.moviment)
            else:
                self.left = 1
                self.position_x = self.position_x+((size/2)*self.moviment)

            pyxel.ellib(self.position_x, self.position_y, size, size, color)

            if not self.left:
                self.left = 0
                self.position_x = self.position_2_x-((size/2)*self.moviment)
            else:
                self.left = 1
                self.position_x = self.position_2_x+((size/2)*self.moviment)

            pyxel.rect(self.position_x, self.position_2_y, size, size, 0)

    def draw(self):
        if self.running:
            size = 20
            self.write_snake(size, self.position_x, self.color)
            if self.position_y > self.height:
                self.color = randint(1,15)
                self.position_y = -30
                self.position_2_y = -30

                if len(self.positions) == 0:
                    self.positions = list(range(0, self.width, 40))
                    if self.moviment == 1:
                        self.moviment = -1
                    else:
                        self.moviment = 1

                self.position_x = choice(self.positions)
                if len(self.positions) > 0:
                    self.positions.remove(self.position_x)

                self.position_2_x = self.position_x

App()