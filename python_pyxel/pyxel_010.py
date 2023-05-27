import pyxel
from random import randint, choice

class Square:
    def __init__(self, x, y, color, size) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def update(self):
        self.y += 1
        if randint(0,1):
            self.x += randint(1,2)
        else:
            self.x -= randint(1,2)
        

class App:

    def __init__(self):
        self.width = 720
        self.height = 1280
        self.running = False
        self.squares = []
        self.size=10
        pyxel.init(self.width, self.height)
        color=7
        x=0
        y=self.size*-1
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
                if s.y>(self.height):
                    if s.color == 7:
                        color = 0
                    else:
                        color = choice([7,13])
                    self.squares.append(Square(s.x,-self.size,color, self.size))
                    self.squares.pop(idx)

        
    def draw(self):
        pyxel.cls(0)
        if self.running:
            for s in self.squares:
                pyxel.rect(s.x, s.y, s.size, s.size, s.color)


App()