# Staci Graham

# Rooms and Items
rooms = {
    'Dining Room': {'North': 'Kitchen', 'East': 'Playroom', 'South': 'Nursery', 'West': 'Office'},
    'Kitchen': { 'South': 'Dining Room', 'East': 'Laundry Room', 'Item': 'Bottle'},
    'Laundry Room': {'West': 'Kitchen', 'Item': 'Pajamas'},
    'Playroom': {'South': 'Bathroom', 'West': 'Dining Room', 'Item': 'Stuffed Animal'},
    'Bathroom': {'North': 'Playroom', 'Item': 'Baby Lotion'},
    'Nursery': {'North': 'Dining Room', 'Item': 'Baby'}, # Villain
    'Office': {'North': 'Living Room', 'East': 'Dining Room', 'Item': 'Book'},
    'Living Room': {'South': 'Office', 'Item': 'Blanket'}
}

# Items List
inventory = []

# Starting Room
current_room = 'Dining Room'

# Show Status
def show_status():
    print(f'You are currently in the {current_room}.')
    print(f'Your current Inventory: {inventory}')

    # Possible Moves
    possible_directions = [key for key in rooms[current_room] if key != 'Item']
    print(f'Possible Direction(s): {possible_directions}')

# Main Menu and Instructions
def show_instructions():
    print('Welcome to Sleepy Time Sprint')
    print('Collect 6 items to complete the bedtime routine for the baby , or a LONG, SLEEPLESS night with a screaming baby awaits!')
    print()
    print('To move rooms, enter: North, East, South or West')
    print('To add an item to Inventory, enter: "Collect item"')
    print('To exit the game, enter: "Exit"')
    print()

# Game Play
def move_between_rooms(current_room):
    show_status()

    if 'Item' in rooms[current_room]:
        item = rooms[current_room]['Item']
        if item not in inventory:
            print(f'You see the {item}.')

    print('---------------------------')
    print()

    # Get User Move
    user_move = input('\nEnter your move: ').capitalize()
    print()

    # Quit
    if user_move == 'Exit':
        print('Thanks for Playing! Goodbye!')
        current_room = False
        return current_room

    # Valid Move
    if user_move in rooms[current_room]:
        current_room = rooms[current_room][user_move]

        # Meeting the Villain
        if current_room == 'Nursery':
            # Win
            if len(inventory) == 6:
                print('Congratulations!! You''ve collected all the items and can successfully complete the baby''s bedtime routine.')
                current_room = False
            # Game Over
            else:
                print('You have reached the baby and are missing items! You''re going to be up ALL NIGHT!')
                print('GAME OVER')
                current_room = False
        return current_room

    # Collect Item
    if user_move == 'Collect item':
        # Not In Inventory
        if item not in inventory:
            inventory.append(item)
            print(f'You have collected the {item}.')
            print()
            return current_room
        # Already Collected
        else:
            print('You''ve already collected this item. Please enter a valid direction to move.')
            print()
            return current_room

    # Move Not Valid
    else:
        print('That is NOT a valid move! Try again.')
        return current_room

# Print Instructions
show_instructions()

# Continue Loop till Exit
while True:
    if current_room == False:
        break
    current_room = move_between_rooms(current_room)