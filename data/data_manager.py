# data_manager.py

import json

class DataManager:
    def __init__(self, data_file="data/sample_data.json"):
        self.data_file = data_file
        self.data = {}
    
    def load_data(self):
        with open(self.data_file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        print(f"Loaded data from {self.data_file}")
    
    def get_npc_data(self):
        return self.data.get("npcs", [])
    
    def get_enemy_data(self):
        return self.data.get("enemies", [])

    def get_level_data(self, level_id):
        """Find and return the level data based on the level ID."""
        for level in self.data.get("levels", []):
            if level["id"] == level_id:
                return level
        return {}  # Return empty if level not found
