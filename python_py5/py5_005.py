import py5
import random
windown_size = width, height = 720, 1280
running = False
size = 5
cordenates_ori = []


def setup():
    py5.size(*windown_size)
    py5.rect_mode(py5.CENTER)
    py5.fill(255)
    py5.background(0)
    py5.color_mode(py5.HSB)
    for x in range(0, py5.width-10, 72):
        for y in range(0, py5.height-10, 128):
            if random.randint(0,1):
                f = py5.circle
            else:
                f = py5.square
            cordenates_ori.append((x,y,f))

    random.shuffle(cordenates_ori)

def draw():
    global running
    py5.stroke(255)
    py5.no_fill()
    py5.background(0)
    if py5.is_key_pressed or running:
        running = True
        for i, (x, y, f) in enumerate(cordenates_ori):
            py5.stroke((i + py5.frame_count)%255, 255, 200)
            d = 50+50 * py5.sin((i+py5.frame_count)/10)
            if d < 10:
                if random.randint(0,1):
                    f = py5.circle
                else:
                    f = py5.square
                cordenates_ori[i] = (cordenates_ori[i][0],cordenates_ori[i][1],f)
            f(x,y,d)


py5.run_sketch()
