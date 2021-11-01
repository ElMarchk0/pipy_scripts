#!/usr/bin/python
import curses # Cursor optimization library for text user interfaces
import threading
import time
DELAY = 0.075
LINES = 40
def printBar(stdscr, y):
    for x in range(LINES):
        # Write contents of y at position y, x * 2
        stdscr.addstr(y, x * 2, str(y))
        stdscr.refresh()
        # Slow down the loop so that effects are easier to observe
        time.sleep(DELAY)
def main(stdscr):
    # Clear the screen
    stdscr.clear()
    # Create 20 threads
    for i in range(20):
      threading.Thread(target = printBar, args = (stdscr, i, )).start()
    # Wait for a key press before exiting
    stdscr.getkey()
    # Wrapper function
curses.wrapper(main) 
