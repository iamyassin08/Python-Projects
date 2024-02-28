name = input("Enter your anime character's name: ")
print("Greetings,", name, "and welcome to this anime adventure!")

answer = input(
    "You find yourself in a mysterious forest. The path diverges, and you must choose: will you go left or right? ").lower()

if answer == "left":
    answer = input(
        "You encounter a mystical river. Will you attempt to cross it or seek an alternate route? Type 'cross' to brave the river or 'avoid' to find another way: ")

    if answer == "cross":
        print("You bravely swim across the river, narrowly avoiding the lurking danger beneath the surface.")
    elif answer == "avoid":
        print("You wander through the forest, exploring alternative paths, but sadly lose your way and the game.")
    else:
        print('Invalid option selected. You lose.')

elif answer == "right":
    answer = input(
        "You stumble upon a precarious bridge. Will you risk crossing it or retreat to safety? (cross/retreat): ")

    if answer == "retreat":
        print("You wisely decide to turn back, but unfortunately lose the game.")
    elif answer == "cross":
        answer = input(
            "You muster your courage and cross the bridge, only to encounter a mysterious figure. Will you engage in conversation? (yes/no): ")

        if answer == "yes":
            print("You engage the stranger in conversation, and they reward you with valuable treasures. Congratulations, you WIN!")
        elif answer == "no":
            print("You choose to avoid the stranger, but unknowingly miss out on a great opportunity, leading to your defeat.")
        else:
            print('Invalid option selected. You lose.')
    else:
        print('Invalid option selected. You lose.')

else:
    print('Invalid option selected. You lose.')

print("Thank you for playing the anime adventure, dear", name)

