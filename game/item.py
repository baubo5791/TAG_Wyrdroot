class Item:
    def __init__(self, name, description, usable=False, value=0):
        self.name = name
        self.description = description
        self.usable = usable
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description}"

    def use(self, player):
        if not self.usable:
            print(f"\nYou can't use the {self.name}.")
        else:
            print(f"\nYou use the {self.name}, but nothing happens... (yet)")