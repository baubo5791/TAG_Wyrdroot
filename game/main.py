from game.player import Player
from game.world_setup import create_world

def main():
    starting_room = create_world()
    player_name = input("\nEnter your name, brave adventurer: ")
    player = Player(player_name, starting_room)

    print(f"\n Welcome, {player.name}!")

    while True:
        player.current_room.describe()

        command = input("\nWhat would you like to do? : ").strip().lower()

        if command in ("quit", "exit"):
            print("\nThanks for playing. Goodbye!")
            break

        elif command.startswith("go "):
            direction = command.split(" ")[1]
            player.move(direction)

        elif command == "look":
            player.current_room.describe()

        elif command.startswith("take "):
            item_name = command.split(" ", 1)[1]
            player.pick_up(item_name)

        elif command.startswith("drop "):
            item_name = command.split(" ", 1)[1]
            player.drop(item_name)

        elif command == "inventory":
            player.show_inventory()

        elif command.startswith("use "):
            item_name = command.split(" ", 1)[1]
            player.use(item_name)

        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()