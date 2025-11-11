import random

elements = {"r": "🪨", "p": "📄", "s": "✂️"}


def get_user_choice():
    while True:
        user = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user not in list(elements.keys()):
            print("Invalid choice")
            continue
        else:
            return user


def display_choices(player, bot):
    print(f"You chose {elements[player]}")
    print(f"Computer chose {elements[bot]}")


def determine_winner(player, bot):
    if player == bot:
        print("Tie")
    elif ((player == "r") & (bot == "p")) or ((player == "p") & (bot == "s")) or ((player == "s") & (bot == "r")):
        print("You lose")
    elif ((player == "r") & (bot == "s")) or ((player == "p") & (bot == "r")) or ((player == "s") & (bot == "p")):
        print("You win")
    else:
        print("Invalid choice!")


def play_game():
    while True:
        player = get_user_choice()
        bot = random.choice(list(elements.keys()))

        display_choices(player, bot)

        determine_winner(player, bot)

        choice = input("Continue? (y/n): ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            break
        else:
            print("Invalid choice, ending program.")
            break


play_game()
