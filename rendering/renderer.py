# renderer.py

from debug import DebugManager, LogLevel

class Renderer:
    def __init__(self, backend='ncurses'):
        self.backend = backend
        debugger = DebugManager()
        debugger.log("Initializing selected Renderer " + backend, LogLevel.INFO)
        if backend == 'ncurses':
            from rendering import NcursesRenderer
            self.renderer = NcursesRenderer()
        elif backend == 'pygame':
            pass  # eventually implement a PygameRenderer @TODO: implement PygameRenderer
        else:
            raise ValueError(f"Invalid renderer backend: {backend}")

    def clear_screen(self):  # Clear the screen
        self.renderer.clear_screen()
