"""
__init__.py

This is the package initialization file for the core package.

It imports and exposes the following modules:
- GameEngine: The main game engine class.
- InputHandler: Handles user input.
- StateManager: Manages game states.

__all__ specifies the public API of the core package.
"""

from .game_engine import GameEngine
from .input_handler import InputHandler
from .state_manager import StateManager

__all__ = ["GameEngine", "InputHandler", "StateManager"]
