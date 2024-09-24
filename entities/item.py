# item.py

class Item:
    def __init__(self, name="Key"):
        self.name = name

    def use(self):
        print(f"You used the {self.name}.")

    def __str__(self):
        return self.name