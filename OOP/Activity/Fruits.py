import random

class Fruits:
    def __init__(self):
        self.fruits = {
            'Apple': 'Red',
            'Banana': 'Yellow',
            'Grapes': 'Green',
            'Orange': 'Orange',
            'Blueberry': 'Blue',
            'Watermelon': 'Green',
            'Strawberry': 'Red',
            'Pineapple': 'Yellow',
            'Mango': 'Yellow',
            'Cherry': 'Red'
        }

    def start(self):
        while True:
            fruit = random.choice(list(self.fruits.keys()))
            color = self.fruits[fruit]
            print(f"\nGuess the color of the {fruit}!")
            ans = input("Your answer: ").strip().lower()

            if ans == color.lower():
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! The color of {fruit} is {color}.")

            play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("Thanks for playing!")
                break


Fruits().start()
