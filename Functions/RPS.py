import random

while True:
    print("1. Rock \n2. Paper \n3. Scissors")
    y = int(input("Choose one of the following (1-3): "))

    x = ["Rock", "Paper", "Scissors"]

    if y < 1 or y > 3:
        print("Invalid choice. Try again.\n")
        continue

    user_action = x[y - 1]
    computer_action = random.choice(x)

    print(f"\nYou have chosen {user_action} and the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    print("\n")
