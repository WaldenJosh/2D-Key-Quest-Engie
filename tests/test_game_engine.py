# test_game_engine.py

import unittest
from core.game_engine import GameEngine

class TestGameEngine(unittest.TestCase):
    def test_start(self):
        engine = GameEngine()
        self.assertTrue(engine.is_running)

if __name__ == '__main__':
    unittest.main()
