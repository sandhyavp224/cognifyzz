import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("The number is higher than your guess.")

        elif guess > number_to_guess:
            print("The number is lower than your guess.")

        else:
            print("Congratulations! You guessed the number correctly.")
            print(f"It took you {attempts} attempts.")
            break   # Exit the loop immediately

    print("Game Over.")

guess_number()