import random

def guess_number():
    number_to_guess = random.randint(1 , 100)
    guess = 0
    attempts = 0
    max_attempts = 10
    print("Welcome to the guessing game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while guess != number_to_guess and attempts <= 10:
        guess = int(input("Guess a number between 1 to 100: "))
        attempts += 1
        if guess < number_to_guess:
            print("to low! Try again!")
            print(f"You're attempts: {attempts}")
        elif guess > number_to_guess:
            print("to high! Try again!")
            print(f"You're attempts: {attempts}")
        else:
            print("Congratulations! You guessed the number correctly!.")
            print(f"It took you {attempts} attempts.")
            
        if attempts == max_attempts and guess != number_to_guess:
            print("You've run out of attempts!")
            print(f"The correct number was {number_to_guess}.")

guess_number()