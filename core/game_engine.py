'''
game_engine.py

This module contains the GameEngine class, which manages the main game loop, rendering, 
and input handling for the 2D Key Quest Engine. It includes methods for starting up, 
updating, rendering, and shutting down the game, as well as managing game status and 
debugging.

Classes:
    GameEngine: Manages the main game loop, rendering, and input handling.

Functions:
    update_status(key, value): Updates the status dictionary with the given key-value pair.
    draw_status_bar(): Draws the status bar on the screen.
    render(): Renders the current game state.
    handle_input(): Handles user input.
    shutdown(): Shuts down the game engine and cleans up resources.
'''
import time
from rendering import Renderer
from debug import DebugManager, LogLevel
from data import data_manager
from core import state_manager
from core import input_handler


status_dict = {
    "frame": 0
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
        self.data_manager = data_manager.DataManager()  # Initialize the data manager
        self.state_manager = state_manager.StateManager()  # Initialize the state manager
        self.input_handler = input_handler.InputHandler()  # Initialize the input handler

    def start_up(self):
        """
        Initializes the game by loading data and setting up states.
        Clears the screen using the renderer.
        """
        self.renderer.clear_screen()
        self.data_manager.load_data()
        self.state_manager.update_level(
            self.data_manager.get_level_data(1))  # Load the first level

    def update(self):
        """
        Updates the game state for the current frame.

        This includes drawing the status bar, updating the status,
        handling input, rendering the frame, and managing frame timing.
        """

        frame_start = time.time()

        self.handle_input()

        self.render()

        elapsed_time = time.time() - frame_start

        if elapsed_time < self.frame_duration:
            time.sleep(self.frame_duration - elapsed_time)

        if status_dict["frame"] == 60:
            status_dict["frame"] = 0
        else:
            status_dict["frame"] += 1

    def update_status(self, key, value):
        """
        Updates the status dictionary with the given key-value pair.

        Args:
            key (str): The key to update in the status dictionary.
            value (Any): The new value to associate with the key.

        Logs an error if the key is not found in the status dictionary.
        """
        if key in status_dict:
            status_dict[key] = value
        else:
            self.debugger.log(
                f"Key {key} not found in status_dict", LogLevel.ERROR)

    def draw_status_bar(self):
        """
        Draws the status bar on the screen.

        This method constructs a status text from the status_dict and uses the renderer
        to draw the text at the specified coordinates (1, 1).
        """
        status_text = " | ".join(
            [f"{key}: {value}" for key, value in status_dict.items()])
        self.renderer.draw_text(1, 1, status_text)

    def draw_level_geometry(self):
        """
        Draws the level geometry on the screen, centered around the player's current position.

        This method retrieves the current level geometry and current position from the state manager.
        The level is drawn such that the current position is centered in the screen.
        """
        # Get the current level data and current position
        level = self.state_manager.return_level()
        current_position = level.get(
            "current_position", [0, 0])  # Get current position

        # Get screen dimensions (width and height)
        screen_width, screen_height = self.renderer.get_screen_size()

        # Calculate the center of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Calculate the top-left corner of where to start drawing the level
        offset_x = center_x - current_position[0]
        offset_y = center_y - current_position[1]

        # Draw the level geometry with the adjusted coordinates
        for row, line in enumerate(level["geometry"]):
            for col, char in enumerate(line):
                # Adjust the position of each tile based on the offsets
                draw_x = col + offset_x
                draw_y = row + offset_y

                # Only draw tiles that are within the screen bounds
                if 0 <= draw_x < screen_width and 0 <= draw_y < screen_height:
                    self.renderer.draw_entity(draw_x, draw_y, char)

    def render(self):
        """
        Renders the current game state by drawing text, a border, and updating the screen.
        """
        # Call the rendering system to draw the current game state
        # Render the level geometry from the state manager self.state_manager.return_level()

        self.renderer.clear_screen()
        self.renderer.draw_border()

        self.draw_status_bar()
        self.draw_level_geometry()
        self.renderer.update_screen()

    # @TODO: implement input handling. I don't have a real input system yet of any kind.

    def handle_input(self):
        """
        Handles user input to control the game.

        Retrieves input from the input handler and stops the game if the 'q' key is pressed.
        """
        key = self.input_handler.get_input()
        if key == ord('q'):
            self.is_running = False

    def shutdown(self):
        """
        Shuts down the game engine by cleaning up resources, saving data, and stopping the renderer.
        """
        self.renderer.shutdown_renderer()
        self.is_running = False
