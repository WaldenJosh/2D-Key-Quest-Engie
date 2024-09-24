# state_manager.py

class StateManager:
    def __init__(self):
        self.current_state = None
    
    def change_state(self, new_state):
        print(f"Changing state to {new_state}")
        self.current_state = new_state
    
    def update(self):
        if self.current_state:
            print("Updating current state...")
            self.current_state.update()
