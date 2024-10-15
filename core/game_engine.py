# game_engine.py

import time
from rendering import Renderer
from debug import DebugManager, LogLevel


status_dict = {
    "test": "testing"
}


class GameEngine:
    """
    The GameEngine class is responsible for managing the main game loop, 
    rendering, and handling input.
    Attributes:
        is_running (bool): Indicates whether the game is currently running.
        renderer (Renderer): An instance of the Renderer class responsible for drawing the game.
        frame_rate (int): The number of frames per second.
        frame_duration (float): The duration of each frame in seconds.
        debugger (DebugManager): An instance of the DebugManager class for logging and debugging.
    """

    def __init__(self):
        self.is_running = True
        self.renderer = Renderer()
        self.frame_rate = 60  # Frames per second
        self.frame_duration = 1.0 / self.frame_rate  # Duration of each frame in seconds
        self.debugger = DebugManager()

    def start_up(self):
        """
        Initializes the game by loading data and setting up states.
        Clears the screen using the renderer.
        """
        self.renderer.clear_screen()

    def update(self):

        frame_start = time.time()

        self.draw_status_bar()
        # This is just for testing. Can be removed soon.
        self.update_status("test", "testing")
        self.handle_input()

        self.render()

        elapsed_time = time.time() - frame_start

        if elapsed_time < self.frame_duration:
            time.sleep(self.frame_duration - elapsed_time)

    def update_status(self, key, value):
        if key in status_dict:
            status_dict[key] = value
        else:
            self.debugger.log(
                f"Key {key} not found in status_dict", LogLevel.ERROR)

    def draw_status_bar(self):
        status_text = " | ".join(
            [f"{key}: {value}" for key, value in status_dict.items()])
        self.renderer.draw_text(1, 1, status_text)

    def render(self):
        # Call the rendering system to draw the current game state
        self.renderer.draw_text(5, 5, "Hello, world!")
        self.renderer.draw_border()
        self.renderer.update_screen()

    # @TODO: implement input handling. I don't have a real input system yet of any kind.
    def handle_input(self):
        key = self.renderer.get_input()
        if key == ord('q'):
            self.is_running = False

    def shutdown(self):
        # Clean up resources, save data, etc.
        self.renderer.shutdown_renderer()
        self.is_running = False
