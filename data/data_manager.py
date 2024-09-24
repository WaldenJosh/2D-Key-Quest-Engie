# data_manager.py

import json

class DataManager:
    def __init__(self, data_file="data/sample_data.json"):
        self.data_file = data_file
        self.data = {}
    
    def load_data(self):
        with open(self.data_file, 'r') as file:
            self.data = json.load(file)
        print(f"Loaded data from {self.data_file}")
    
    def get_npc_data(self):
        return self.data.get("npcs", [])
    
    def get_enemy_data(self):
        return self.data.get("enemies", [])
