# state_manager.py

class StateManager:
    def __init__(self):
        self.current_state = None
    
    def update_level(self, level):
        self.current_state = level
        print(f"Updated current state to {level}")
