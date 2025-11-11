import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number")
