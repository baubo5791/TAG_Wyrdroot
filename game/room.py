class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def link_room(self, direction, room):
        self.exits[direction] = room

    def get_room_in_direction(self, direction):
        return self.exits.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def describe(self):
        print(f"\n== {self.name} ==")
        print(self.description)

        if self.items:
            print("\nYou see the following items:")
            for item in self.items:
                print(f" - {item.name}")

        if self.exits:
            print("\nExits:")
            for direction in self.exits:
                print(f" - {direction}")
