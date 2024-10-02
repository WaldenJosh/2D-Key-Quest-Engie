# main.py

from core.game_engine import GameEngine
from debug import DebugManager, LogLevel

debugger = DebugManager()

if __name__ == "__main__":
    debugger.log("Starting the game engine...", LogLevel.INFO)
    engine = GameEngine()
    engine.start_up()
    
    engine.render()

    while engine.is_running:
        engine.update()

    engine.shutdown()
