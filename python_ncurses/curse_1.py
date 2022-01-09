import sys,os
import curses
from time import sleep

def animate(screen, desenho):
    screen.clear()
    screen.attron(curses.color_pair(3))
    height, width = screen.getmaxyx()
    desenho = open('./desenhos/iron_man.txt', 'r')
    lines = desenho.readlines()
    linha = 0
    coluna = 0
    for l in lines:
        linha += 1
        coluna = 0
        for c in l:
            sleep(0.01)
            if c == "3":
                screen.attron(curses.color_pair(3))
            elif c == "4":
                screen.attron(curses.color_pair(4))
            elif c == "1":
                screen.attron(curses.color_pair(1))
            else:
                screen.addstr(linha, coluna, c)
                screen.refresh()
                coluna +=1

    screen.attroff(curses.color_pair(3))
    

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()

    curses.init_color(6, 1000, 616, 0)
    curses.init_color(5, 1000, 616, 0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    
    curses.init_pair(3, 6, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        if k == ord('r'):
            animate(stdscr, 2)

        # Initialization
       
        height, width = stdscr.getmaxyx()
        statusbarstr = "'q' to exit | 'r' to run ".format(cursor_x, cursor_y)
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(0, 0, statusbarstr)
        stdscr.addstr(0, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(2))
        stdscr.refresh()
        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()