# renderer.py

from debug import DebugManager, LogLevel


class Renderer:
    def __init__(self, backend='ncurses'):
        self.backend = backend
        self.debugger = DebugManager()
        self.debugger.log("Initializing selected Renderer " +
                     backend, LogLevel.INFO)
        if backend == 'ncurses':
            from rendering import NcursesRenderer
            self.renderer = NcursesRenderer()
        elif backend == 'pygame':
            pass  # eventually implement a PygameRenderer @TODO: implement PygameRenderer
        else:
            raise ValueError(f"Invalid renderer backend: {backend}")

    def clear_screen(self):  # Clear the screen
        self.renderer.clear_screen()
        self.debugger.log("Clearing the screen...", LogLevel.INFO)

    # Draw a character on the screen at the specified position
    def draw_entity(self, x, y, char):
        self.renderer.draw_entity(x, y, char)
        self.debugger.log(f"Drawing entity at ({x}, {y})...", LogLevel.INFO)

    def draw_text(self, x, y, text):  # Draw text on the screen at the specified position
        self.renderer.draw_text(x, y, text)
        self.debugger.log(f"Drawing text at ({x}, {y})...", LogLevel.INFO)

    def draw_border(self):  # Draw a border around the screen
        self.renderer.draw_border()
        self.debugger.log("Drawing border...", LogLevel.INFO)

    def display_message(self, message):  # Display a message in the center of the screen
        self.renderer.display_message(message)
        self.debugger.log(f"Displaying message: {message}...", LogLevel.INFO)

    def update_screen(self):  # Refresh the screen
        self.renderer.update_screen()
        self.debugger.log("Updating screen...", LogLevel.INFO)

    def shutdown_renderer(self):  # Shut down the renderer and clean up
        self.renderer.shutdown_renderer()
        self.debugger.log("Shutting down renderer...", LogLevel.INFO)

    def handle_resize(self):  # Handle a resize event
        self.renderer.handle_resize()
        self.debugger.log("Handling resize...", LogLevel.INFO)

    def get_screen_size(self):  # Get the screen size
        self.debugger.log("Getting screen size...", LogLevel.INFO)
        return self.renderer.get_screen_size()

    def get_input (self): # Get input from the user
        self.debugger.log("Getting input...", LogLevel.INFO)
        return self.renderer.get_input()
    
