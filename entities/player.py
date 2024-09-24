# player.py

class Player:
    def __init__(self, name="Player", hp=100):
        self.name = name
        self.hp = hp
    
    def move(self, direction):
        print(f"{self.name} is moving {direction}")
    
    def attack(self, target):
        print(f"{self.name} attacks {target}")
