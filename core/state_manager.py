# state_manager.py

class StateManager:
    def __init__(self):
        # Initialize the state dictionary
        self.state = {
            "current_level": {
                "id": None,
                "geometry": [],
            },
            "player": {
                "id": None,
                "name": "",
                "hp": 0,
                "attack": 0,
                "defense": 0,
                "inventory": []
            },
            "npcs": {},
            "enemies": {},
            "doors": {},
            "keys": {},
            "items": {},
            "level_entities": {
                "npcs": [],
                "enemies": [],
                "doors": [],
                "keys": [],
                "items": []
            }
        }

    def update_level(self, level):
        # Update the current level
        self.state["current_level"] = level
