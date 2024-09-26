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
        self.debugger.log("Initializing ncurses renderer...", LogLevel.INFO)
        self.height, self.width = self.stdscr.getmaxyx()
    
    def clear_screen(self):
        """Clear the ncurses screen."""
        self.stdscr.clear()
        self.debugger.log("Clearing the screen...", LogLevel.INFO)
    
    def draw_entity(self, x, y, char):
        """Draw a character on the screen at the specified position."""
        try:
            self.stdscr.addch(y, x, char)
            self.debugger.log(f"Drawing entity at ({x}, {y})...", LogLevel.INFO)
        except curses.error:
            self.debugger.log(f"Failed to draw entity at ({x}, {y})...", LogLevel.ERROR)
            pass  # Handle edge cases like drawing off-screen
    
    def draw_text(self, x, y, text):
        try:
            self.stdscr.addstr(y, x, text)
            self.debugger.log(f"Drawing text at ({x}, {y})...", LogLevel.INFO)
        except curses.error:
            self.debugger.log(f"Failed to draw text at ({x}, {y})...", LogLevel.ERROR)
            pass

    def draw_border(self):
        try:
            self.stdscr.border()
            self.debugger.log("Drawing border...", LogLevel.INFO)
        except curses.error:
            self.debugger.log("Failed to draw border...", LogLevel.ERROR)
            pass

    def display_message(self, message):
        try:
            y, x = self.height // 2, self.width // 2 - len(message) // 2
            self.stdscr.addstr(y, x, message)
            self.debugger.log(f"Displaying message: {message}...", LogLevel.INFO)
        except curses.error:
            self.debugger.log("Failed to display message...", LogLevel.ERROR)
            pass

    def update_screen(self):
        """Refresh the screen to display any changes."""
        self.stdscr.refresh()
        self.debugger.log("Updating screen...", LogLevel.INFO)
    
    def shutdown_renderer(self):
        """Restore terminal settings and shutdown ncurses."""
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        self.debugger.log("Shutting down ncurses renderer...", LogLevel.INFO)

    def get_screen_size(self):
        return self.stdscr.getmaxyx()
    
    def handle_resize(self):
        self.height, self.width = self.stdscr.getmaxyx()
        self.stdscr.clear()
        self.debugger.log(f"Screen resized to {self.width}x{self.height}...", LogLevel.INFO)