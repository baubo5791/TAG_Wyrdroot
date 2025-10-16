from game.room import Room
from game.item import Item

def create_world():
    # Create rooms
    cave = Room("Cave Entrance", "A damp, cold cave. The air smells of sulfur.")
    hall = Room("Dark Hallway", "A shadowy corridor, lit by flickering torches.")
    armory = Room("Old Armory", "Dusty weapons line the walls.")

    # Link rooms
    cave.link_room("north", hall)
    hall.link_room("south", cave)
    hall.link_room("east", armory)
    armory.link_room("west", hall)

    # Create items
    sword = Item("Sword", "A rusty sword. Still sharp.", usable=False, value=10)
    potion = Item("Potion", "Heals 20 HP.", usable=True, value=20)

    # Add items to rooms
    cave.add_item(potion)
    armory.add_item(sword)

    return cave  # starting room