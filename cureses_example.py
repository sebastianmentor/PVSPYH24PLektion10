import curses
import time

def main(stdscr):
    while True:
    # Rensa skärmen
        stdscr.clear()

        # Vänta på att användaren trycker på en tangent
        stdscr.addstr("Tryck på en tangent...")
        stdscr.refresh()

        # Läs in tangenttrycket
        key = stdscr.getch()
        # with open("keystroke.txt", "a") as f:
        #     # f.write(chr(key) + '\n')
        #     f.write(str(key) + '\n')

        # Visa det tryckta tecknet (eller koden för specialtangenter)
        stdscr.addstr(f"Du tryckte: {key}")

        if key == curses.KEY_LEFT:
            stdscr.addstr(f"Du tryckte: Vänster pilknapp")
            
        stdscr.refresh()
        # time.sleep(0.5)
        if key==113:
            break
        # Vänta innan avslut
        stdscr.getch()

# Kör curses-programmet
curses.wrapper(main)
