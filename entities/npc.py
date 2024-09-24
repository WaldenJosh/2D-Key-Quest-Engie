# npc.py

class NPC:
    def __init__(self, name="Villager", dialogue="Hello there!"):
        self.name = name
        self.dialogue = dialogue
    
    def talk(self):
        print(f"{self.name} says: '{self.dialogue}'")
