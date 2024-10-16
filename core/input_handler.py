"""
This module implements the input handling for the 2D Key Quest Engine.
Classes:
    InputHandler: Handles capturing and processing player input.
The InputHandler class interacts with the renderer system to get input 
from the currently utilized rendering engine.
"""
from rendering import Renderer


class InputHandler:
    """
    Handles player input and maps it to game functions.
    """

    def __init__(self):
        self.renderer = Renderer()

    def get_input(self):
        """
        Retrieves input from the renderer.

        Returns:
            Any: The input data obtained from the renderer.
        """
        return self.renderer.get_input()
