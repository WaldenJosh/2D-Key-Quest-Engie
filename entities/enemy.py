# enemy.py

class Enemy:
    def __init__(self, enemy_type="Goblin", hp=30):
        self.enemy_type = enemy_type
        self.hp = hp
    
    def move(self):
        print(f"{self.enemy_type} is moving")
    
    def attack(self, target):
        print(f"{self.enemy_type} attacks {target}")
