import random

def guess_the_number():
    number_to_guess = random.randint(1, 50)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
guess_the_number()