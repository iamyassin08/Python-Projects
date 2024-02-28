# Prompt the user to enter their anime character's name
name = input("Enter your anime character's name: ")

# Greet the user with their entered name
print("Greetings,", name, "and welcome to this anime adventure!")

# Prompt the user to choose a direction in the mysterious forest and convert the input to lowercase
answer = input(
    "You find yourself in a mysterious forest. The path diverges, and you must choose: will you go left or right? ").lower()

# Check the user's choice
if answer == "left":
    # If the user chooses to go left, prompt them to decide how to deal with a mystical river
    answer = input(
        "You encounter a mystical river. Will you attempt to cross it or seek an alternate route? Type 'cross' to brave the river or 'avoid' to find another way: ")

    # Check the user's choice regarding the river
    if answer == "cross":
        # If the user chooses to cross the river, print a message indicating successful crossing
        print("You bravely swim across the river, narrowly avoiding the lurking danger beneath the surface.")
    elif answer == "avoid":
        # If the user chooses to avoid the river, print a message indicating the consequence
        print("You wander through the forest, exploring alternative paths, but sadly lose your way and the game.")
    else:
        # If the user enters an invalid choice, print a message indicating loss
        print('Invalid option selected. You lose.')

elif answer == "right":
    # If the user chooses to go right, prompt them to decide how to deal with a precarious bridge
    answer = input(
        "You stumble upon a precarious bridge. Will you risk crossing it or retreat to safety? (cross/retreat): ")

    # Check the user's choice regarding the bridge
    if answer == "retreat":
        # If the user chooses to retreat, print a message indicating loss
        print("You wisely decide to turn back, but unfortunately lose the game.")
    elif answer == "cross":
        # If the user chooses to cross the bridge, prompt them to decide how to interact with a stranger
        answer = input(
            "You muster your courage and cross the bridge, only to encounter a mysterious figure. Will you engage in conversation? (yes/no): ")

        # Check the user's choice regarding the conversation with the stranger
        if answer == "yes":
            # If the user chooses to engage in conversation, print a message indicating victory
            print("You engage the stranger in conversation, and they reward you with valuable treasures. Congratulations, you WIN!")
        elif answer == "no":
            # If the user chooses not to engage in conversation, print a message indicating defeat
            print("You choose to avoid the stranger, but unknowingly miss out on a great opportunity, leading to your defeat.")
        else:
            # If the user enters an invalid choice, print a message indicating loss
            print('Invalid option selected. You lose.')
    else:
        # If the user enters an invalid choice, print a message indicating loss
        print('Invalid option selected. You lose.')

else:
    # If the user enters an invalid choice for the initial direction, print a message indicating loss
    print('Invalid option selected. You lose.')

# Print a closing message to thank the user for playing the game
print("Thank you for playing the anime adventure, dear", name)
