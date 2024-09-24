# test_level_generator.py

import unittest
from procedural.level_generator import LevelGenerator

class TestLevelGenerator(unittest.TestCase):
    def test_generate_level(self):
        generator = LevelGenerator()
        generator.generate_level()
        # You could add more specific assertions based on actual generation

if __name__ == '__main__':
    unittest.main()
