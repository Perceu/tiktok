import pyxel
from random import randint, randrange, getrandbits

class Drop:
    x=0
    y=0
    visible = True

    def __init__(self, height, width, colors):
        self.size = randint(3, 10)
        self.height = height
        self.width = width
        self.colors = colors
        self.y = randint(self.height*-1,0 )
        spaces = self.width/10
        self.x = randrange(0, int(spaces*10), self.size)
        self.velocity = randint(self.size, self.size*2)

    def update(self):
        self.y += self.velocity

        if self.y > self.height:
            self.visible = False
    
    def draw(self):
        for index, _ in enumerate(self.colors):
            position_y = self.y - (index*-self.size)
            pyxel.rect(self.x, position_y, self.size, self.size, index)
        

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
            0x001900,
            0x000000,
        ][::-1]

        pyxel.colors.from_list(self.colors)
        self.drops = []
        for _ in range(500):
            self.drops.append(Drop(self.height, self.width, self.colors))
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.running = True
        

    def draw(self):
        pyxel.cls(0)
        if self.running:
            for index, drop in enumerate(self.drops):
                drop.update()
                drop.draw()
                if not drop.visible:
                    self.drops.pop(index)
                    self.drops.append(Drop(self.height,self.width, self.colors))

App()