# Gary Hobson
# IT 140 Module Six Milestone: Simplified Ghost Ship Quest - Move Between Rooms

# Dictionary mapping rooms to connected rooms (simplified from Project One map)
rooms = {
    'Deck': {'South': 'Crew’s Quarters'},
    'Crew’s Quarters': {'North': 'Deck', 'East': 'Cargo Hold'},
    'Cargo Hold': {'West': 'Crew’s Quarters'}
}

# Initialize starting room
current_room = 'Deck'

# Gameplay loop: Continue until player exits
while current_room != 'exit':
    # Display current room
    print(f"You are in the {current_room}")
    
    # Prompt for user input (e.g., go South, exit)
    user_input = input("Enter your move: ").strip().lower()
    
    # Check for exit command
    if user_input == 'exit':
        current_room = 'exit'
    # Check for move command (e.g., go south)
    elif user_input.startswith('go '):
        # Extract direction after "go" (e.g., "south")
        direction = user_input[3:].strip().capitalize()  # Capitalize for dictionary match
        
        # Validate direction and move if valid
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")  # Invalid direction
    else:
        print("Invalid Input!")  # Invalid command format
    
# Game ends when player exits
print("Thanks for playing Ghost Ship Quest!")