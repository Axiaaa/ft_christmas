import curses, random, time

def snow_fall(stdscr):
    curses.curs_set(0) 
    stdscr.nodelay(1), stdscr.timeout(1) 

    height, width = stdscr.getmaxyx()
    snowflakes = []

    while True:
        x = random.randint(0, width - 1)
        snowflakes.append((0, x))
        stdscr.clear()
        new_snowflakes = []
        for y, x in snowflakes:
            stdscr.addstr(y, x, "*")
            if y + 1 < height:
                new_snowflakes.append((y + 1, x))
        snowflakes = new_snowflakes
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        time.sleep(0.3)

curses.wrapper(snow_fall)
