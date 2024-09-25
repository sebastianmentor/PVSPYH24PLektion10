import curses
import random

def main(stdscr):
    # Inaktivera kursorn
    curses.curs_set(0)
    # Få storleken på terminalen
    sh, sw = stdscr.getmaxyx()
    # Rita en ram runt hela skärmen
    stdscr.border()
    # Startposition för myran (innanför ramen)
    ant_x = sw // 2
    ant_y = sh // 2
    # Startpoäng
    score = 0
    # Placera första sockerbiten (innanför ramen)
    sugar_x = random.randint(1, sw - 2)
    sugar_y = random.randint(1, sh - 2)
    # Ställ in icke-blockerande input
    stdscr.nodelay(1)
    # Spelloopen
    while True:
        stdscr.clear()
        # Rita ramen
        stdscr.border()
        # Rita myran
        stdscr.addstr(ant_y, ant_x, "A")
        # Rita sockerbiten
        stdscr.addstr(sugar_y, sugar_x, "*")
        # Visa poängen
        stdscr.addstr(0, 2, f" Poäng: {score} ")
        stdscr.refresh()
        # Vänta på input
        key = stdscr.getch()
        # Hantera input
        if key == curses.KEY_UP:
            ant_y -= 1
        elif key == curses.KEY_DOWN:
            ant_y += 1
        elif key == curses.KEY_LEFT:
            ant_x -= 1
        elif key == curses.KEY_RIGHT:
            ant_x += 1
        elif key == ord('q'):
            break
        # Håll myran inom ramen
        ant_x = max(1, min(ant_x, sw - 2))
        ant_y = max(1, min(ant_y, sh - 2))
        # Kolla om myran äter sockerbiten
        if ant_x == sugar_x and ant_y == sugar_y:
            score += 1
            sugar_x = random.randint(1, sw - 2)
            sugar_y = random.randint(1, sh - 2)
        # Vänta lite för att sakta ner spelet
        curses.napms(5)

curses.wrapper(main)
