# Gary Hobson
# IT 140 Project Two: Haunted Ghost Ship Text Based Adventure Game

# Dictionary mapping rooms to directions and items (from Project One map)
rooms = {
    'Deck': {'South': 'Sick Bay', 'East': 'Crew’s Quarters', 'North': 'Armory', 'item': None},
    'Crew’s Quarters': {'West': 'Deck', 'East': 'Galley', 'South': 'Cargo Hold', 'item': 'Compass'},
    'Galley': {'West': 'Crew’s Quarters', 'item': 'Spyglass'},
    'Cargo Hold': {'North': 'Crew’s Quarters', 'South': 'Captain’s Quarters', 'item': 'Cutlass'},
    'Captain’s Quarters': {'North': 'Cargo Hold', 'item': None, 'villain': 'Ghost of the Pirate Captain'},
    'Sick Bay': {'North': 'Deck', 'item': 'Amulet'},
    'Armory': {'South': 'Deck', 'North': 'Crow’s Nest', 'item': 'Pistol'},
    'Crow’s Nest': {'South': 'Armory', 'item': 'Map'}
}

def show_instructions():
    """Display game title, goal, and commands."""
    print("The Haunted Ghost Ship ")
    print("Collect 6 sacred artifacts to lift the curse and defeat the Ghost of the Pirate Captain.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

def show_status(current_room, inventory):
    """Show player's status: current room, inventory, and item in room."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if rooms[current_room]['item'] is not None:
        print(f"You see a {rooms[current_room]['item']}")

def main():
    """Main game loop: handle movement, item collection, and win/loss conditions."""
    # Initialize starting room and inventory
    current_room = 'Deck'
    inventory = []
    
    # Show instructions at start
    show_instructions()
    
    # Gameplay loop: Continue until win or loss
    while True:
        # Show player status
        show_status(current_room, inventory)
        
        # Prompt for user input (go South, get Compass, exit)
        user_input = input("Enter your move: ").strip().lower()
        
        # Check for exit command
        if user_input == 'exit':
            print("Thanks for playing Haunted Ghost Ship!")
            break
        
        # Check for move command (go south)
        elif user_input.startswith('go '):
            # Extract direction after "go" ("south")
            direction = user_input[3:].strip().capitalize()  # Capitalize for dictionary match
            
            # Validate direction and move if valid
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                
                # Check win/loss condition after moving
                if current_room == 'Captain’s Quarters':
                    if len(inventory) == 6:  # All items collected
                        print("Congratulations! You have collected all artifacts and defeated the Ghost of the Pirate Captain!")
                        print("Thanks for playing Haunted Ghost Ship!")
                        break
                    else:  # Entered villain room without all items
                        print("ARGH! The the Ghost of the Pirate Captain curses you...GAME OVER!")
                        print("Thanks for playing Haunted Ghost Ship!")
                        break
            else:
                print("You can't go that way!") 
        
        # Check for get item command (get compass)
        elif user_input.startswith('get '):
            # Extract item after "get" ("compass")
            item = user_input[4:].strip().capitalize()  # Capitalize for match
            
            # Validate item and add to inventory if valid
            if rooms[current_room]['item'] is None:
                print("No item to get!")
            elif item == rooms[current_room]['item']:
                inventory.append(item)
                print(f"{item} retrieved!")
                rooms[current_room]['item'] = None  # Remove item from room
            else:
                print(f"Can't get {item}!")  # Invalid item
        
        else:
            print("Invalid Input!")  # Invalid command format

# Run the game
if __name__ == "__main__":
    main()