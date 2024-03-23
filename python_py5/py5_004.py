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
    for x in range(0, py5.width-10, 100):
        for y in range(0, py5.height-10, 100):
            cordenates_ori.append((x,y))


def draw():
    global running
    py5.background(0)
    py5.stroke(255)
    if py5.is_key_pressed or running:
        running = True
        for i, (x, y) in enumerate(cordenates_ori):
            py5.fill((i + py5.frame_count)%180, 95)
            d = 50+50 * py5.sin((i+py5.frame_count)/10)
            if i%2:
                py5.square(x,y,d)
            else:
                py5.circle(x,y,d)


py5.run_sketch()
