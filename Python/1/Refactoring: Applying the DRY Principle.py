# The DRY or don't repeat yourself principle (make variables if used more than once)
import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
elements = {"r": "🪨", "p": "📄", "s": "✂️"}
keys = list(elements.keys())


def get_user_choice():
    while True:
        user = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user not in keys:
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
    elif ((player == ROCK) & (bot == PAPER)) or ((player == PAPER) & (bot == SCISSORS)) or ((player == SCISSORS) & (bot == ROCK)):
        print("You lose")
    elif ((player == ROCK) & (bot == SCISSORS)) or ((player == PAPER) & (bot == ROCK)) or ((player == SCISSORS) & (bot == PAPER)):
        print("You win")
    else:
        print("Invalid choice!")


def play_game():
    while True:
        player = get_user_choice()
        bot = random.choice(keys)

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
