class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.health_points = 100
        self.max_health_points = 100
        self.attack_power = 10

    def is_alive(self):
        return self.health_points > 0

    def move(self, direction):
        if self.is_alive():
            next_room = self.current_room.get_room_in_direction(direction)
            if next_room:
                self.current_room = next_room
                print(f"\nYou moved {direction} to {self.current_room.name}")
            else:
                print("\nYou cannot go that way.")

    def show_inventory(self):
        if not self.inventory:
            print("\nYour inventory is empty.")
            return
        print("\nInventory:")
        for item in self.inventory:
            print(f"- {item.name}")

    def pick_up(self, item_name):
        item = self.current_room.get_item(item_name)
        if item:
            self.inventory.append(item)
            self.current_room.remove_item(item)
            print(f"\nYou picked up {item.name}")
        else:
            print("\nThere is no such item here.")

    def drop(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.current_room.add_item(item)
                print(f"\nYou dropped {item.name}")
                return
        print("\nYou don't have that item.")

    def attack(self, enemy):
        damage = self.attack_power
        enemy.take_damage(damage)
        print(f"\nYou attacked the {enemy.name} for {damage} damage.")

    def use(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                return
        print("\nYou don't have that item.")
