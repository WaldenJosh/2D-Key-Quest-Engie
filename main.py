"""
main.py

This module initializes and runs the 2D Key Quest game engine. It sets up the 
debug manager, starts the game engine, and handles the game loop until the 
engine is shut down.
"""

from core.game_engine import GameEngine
from debug import DebugManager, LogLevel

debugger = DebugManager()

if __name__ == "__main__":
    debugger.log("Starting the game engine...", LogLevel.INFO)
    engine = GameEngine()
    engine.start_up()

    while engine.is_running:
        engine.update()

    engine.shutdown()
