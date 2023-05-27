import pyxel
from random import randint

class Square:
    def __init__(self, x, y, color, size) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def update(self):
        if (self.y < (self.y + self.size)):
            self.y += 1
            self.y += 1
        

class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False
        self.squares = []
        self.cicles = 150000
        self.size=30
        pyxel.init(self.width, self.height)
        color=7
        x=0
        y=0
        while True:
            if (color==7):
                color = 0
            else:
                color = 7
            self.squares.append(Square(x,y,color, self.size))
            x += self.size
            if x > self.width:
                x = 0
                y += self.size
                if y > self.height:
                    break

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True
            
        if self.running:
            for idx, s in enumerate(self.squares):
                s.update()
                if s.y>self.height:
                    if s.color != 0 and s.color != 7:
                        color = 0
                    elif s.color == 7:
                        color = 0
                    else:
                        color = randint(1,15)
                    self.squares.append(Square(s.x,0,color, self.size))
                    self.squares.pop(idx)

        
    def draw(self):
        pyxel.cls(0)
        if self.running:
            for s in self.squares:
                if self.cicles < 0:
                    pyxel.rectb(s.x, s.y, s.size, s.size, s.color)
                else:
                    pyxel.rect(s.x, s.y, s.size, s.size, s.color)
                self.cicles -= 1
                if self.cicles < -150000:
                    self.cicles = 150000


App()