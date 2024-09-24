# ncurses_renderer.py

import curses
from rendering import Renderer

class NcursesRenderer(Renderer):
    def draw_entity(self, entity):
        print(f"Rendering {entity} with ncurses")
    
    def draw_map(self, game_map):
        print(f"Rendering map with ncurses: {game_map}")
        # Here, ncurses-specific rendering logic would go
