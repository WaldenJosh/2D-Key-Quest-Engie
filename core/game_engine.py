# game_engine.py

from rendering import Renderer

class GameEngine:
    def __init__(self):
        self.is_running = True
        self.renderer = Renderer()
    
    def start(self):
        print("Starting the 2D Key Quest Engine...")
        # Initialize the game, load data, set up states
        self.renderer.clear_screen()
    
    def update(self):
        print("Updating game state...")
        # Logic for updating game state

    def render(self):
        print("Rendering the game...")
        # Call the rendering system to draw the current game state
        self.renderer.draw_text(5, 5, "Hello, world!")
        self.renderer.update_screen()
    
    def handle_input(self): # @TODO: implement input handling. I don't have a real input system yet of any kind.
        print("Handling input...")
        key = self.renderer.get_input()
        if key == ord('q'):
            self.shutdown()

    def shutdown(self):
        print("Shutting down the game engine...")
        # Clean up resources, save data, etc.
        self.renderer.shutdown_renderer()
        self.is_running = False
