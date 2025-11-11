import random

elements = {"r": "🪨", "p": "📄", "s": "✂️"}

while True:
    player = input("Rock, paper, or scissors? (r/p/s): ").lower()
    bot = random.choice(list(elements.keys()))

    print(f"You chose {elements[player]}")
    print(f"Computer chose {elements[bot]}")

    if player == bot:
        print("Tie")
    elif (player == "r") & (bot == "p"):
        print("You lose")
    elif (player == "r") & (bot == "s"):
        print("You win")
    elif (player == "p") & (bot == "r"):
        print("You win")
    elif (player == "p") & (bot == "s"):
        print("You lose")
    elif (player == "s") & (bot == "r"):
        print("You lose")
    elif (player == "s") & (bot == "p"):
        print("You win")
    else:
        print("Invalid choice!")

    choice = input("Continue? (y/n): ").lower()
    if choice == "y":
        continue
    elif choice == "n":
        break
    else:
        print("Invalid choice, ending program.")
