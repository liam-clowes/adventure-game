### MY ADVENTURE GAME

import random

# WELCOME MESSAGE
print("""
Find your wallet so that you can get to Spiced on time for your first encounter of the day
===================

Your quest starts now.
""")

# DEFINE VARIABLES
room = 0
wallet = False

# DICTIONARIES
room_descriptions = {
    0: "You are on Hermannstraße, but you left your wallet back at your flat. Head back upstairs to find it",
    1: "You entered the KITCHEN. You found your lunch, but no sign of your wallet",
    2: "You entered the LIVING ROOM. No sign of a wallet here",
    3: "You entered the BATHROOM. Now why would your wallet be here? Only one place it could be...",
    4: "It's always in the last place you look - the BEDROOM!",
}

wallet_locations = ["KITCHEN", "LIVING ROOM", "BATHROOM", "BEDROOM"]
random.shuffle(wallet_locations)

# MAIN GAME LOOP
while room != 4:
    print(room_descriptions[room])

    if not wallet and room == wallet_locations.index("BEDROOM"):
        print("Hint: Check the BEDROOM carefully.")

    action = input("Enter 'forward' to move forward, 'back' to move back: ").lower()

    if action == "forward" and room < 4:
        room += 1
    elif action == "back" and room > 0:
        room -= 1
    else:
        print("Invalid command.")

# End game message
print("""
Your wallet was under a pile of clean laundry in your BEDROOM. Great!\nYou can deal with the laundry later - better run to the U8 now! 

Your quest has been successful!
""")
