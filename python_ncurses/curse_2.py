import sys,os
import curses
from time import sleep

def animate(screen, desenho):
    screen.clear()
    desenho = open('./desenhos/batman.txt', 'r')
    lines = desenho.readlines()
    linha = len(lines)
    coluna = 0
    for l in lines[::-1]:
        linha -= 1
        coluna = 0
        for c in l:
            sleep(0.004)
            if c == "1":
                screen.attron(curses.color_pair(1))
            elif c == "2":
                screen.attron(curses.color_pair(2))
            elif c == "3":
                screen.attron(curses.color_pair(3))
            else:
                screen.addstr(linha, coluna, c)
                screen.refresh()
                coluna +=1
    

def draw_screen(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    
    # Loop where k is the last character pressed
    while (k != ord('q')):

        if k == ord('r'):
            animate(stdscr, 2)
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            animate(stdscr, 2)

        stdscr.refresh()
        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(draw_screen)

if __name__ == "__main__":
    main()