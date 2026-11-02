# random number guesser

import random

random_number = random.randint(1, 100) # generates a random number between 1 and 100

game = True
guesses = []

while game:
    guess = int(input("Guess a number between 1 and 100: ")) # takes user input for guess

    if guess < 1 or guess > 100: # checks for valid number between 1 and 100
        print("Invalid guess. Please enter a number between 1 and 100.")

        guesses.append(guess) # adds guess to list of guesses

        if guess < random_number: # checks if guess is less than random number
            print("Too low! Try again.")
        elif guess > random_number: # checks if guess is greater than random number
            print("Too high! Try again.")
        else: # if guess is not less than or greater than random number, it must be equal to random number
            print(f"Congratulations! You guessed the number {random_number} in {len(guesses)} tries.")
            game = False

    else:
        print("Invalid guess. Please enter a number between 1 and 100.")
