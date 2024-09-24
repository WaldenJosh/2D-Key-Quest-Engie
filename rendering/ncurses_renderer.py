# ncurses_renderer.py

import curses
from debug import DebugManager, LogLevel

class NcursesRenderer:
    def __init__(self):
        """Initialize ncurses and set up the screen."""
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)
        self.stdscr.clear()
        self.debugger = DebugManager()
    
    def clear_screen(self):
        """Clear the ncurses screen."""
        self.stdscr.clear()
        self.debugger.log("Clearing the screen...", LogLevel.INFO)
    
    def draw_entity(self, x, y, char):
        """Draw a character on the screen at the specified position."""
        try:
            self.stdscr.addch(y, x, char)
        except curses.error:
            pass  # Handle edge cases like drawing off-screen
    
    def update_screen(self):
        """Refresh the screen to display any changes."""
        self.stdscr.refresh()
    
    def shutdown_renderer(self):
        """Restore terminal settings and shutdown ncurses."""
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()