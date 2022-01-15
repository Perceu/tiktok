import curses
from time import sleep

def animate(screen, desenho):
    screen.clear()
    desenho = open('./desenhos/superman.txt', 'r')
    lines = desenho.readlines()
    position_x = (len(lines)-1)
    position_y = 0
    
    while True:
        sleep(0.006)
        try:
            c = lines[position_x][position_y]
        except Exception as e:
            break
        
        position_x -= 1

        if c == "1":
            screen.attron(curses.color_pair(1))
            continue
        elif c == "2":
            screen.attron(curses.color_pair(2))
            continue
        elif c == "3":
            screen.attron(curses.color_pair(3))
            continue
        else:
            screen.addstr(int((position_x+1)/2), position_y, c)
            screen.refresh()

        if position_x < 0:
            position_x = (len(lines)-1)
            position_y += 1

def draw_screen(stdscr):
    k = 0
    stdscr.clear()
    stdscr.refresh()
    # Start colors in curses
    curses.start_color()
    curses.init_color(10, 1000, 0, 0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(2, 10, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    
    # Loop where k is the last character pressed
    while (k != ord('q')):

        if k == ord('r'):
            animate(stdscr, 2)

        stdscr.refresh()
        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_screen)

if __name__ == "__main__":
    main()