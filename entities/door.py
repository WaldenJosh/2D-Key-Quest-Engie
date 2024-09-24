# door.py

class Door:
    def __init__(self, name="Door", locked=True):
        self.name = name
        self.locked = locked

    def unlock(self):
        self.locked = False
        print(f"{self.name} is now unlocked.")

    def open(self):
        if self.locked:
            print(f"{self.name} is locked.")
        else:
            print(f"{self.name} is now open.")

    def __str__(self):
        return self.name