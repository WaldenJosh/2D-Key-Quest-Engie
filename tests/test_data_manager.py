# test_data_manager.py

import unittest
from data.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def test_load_data(self):
        manager = DataManager()
        manager.load_data()
        self.assertIn("npcs", manager.data)

if __name__ == '__main__':
    unittest.main()
