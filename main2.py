import random

def get_random_greeting():
    greetings = [
        "Welcome to Python!",
        "Hello, Pythonista!",
        "Ahoy! Ready for Python?",
        "Greetings!",
        "Python welcomes you with open arms!"
    ]
    return random.choice(greetings)

def main():
    print(get_random_greeting())
    name = input("Enter your name: ")
    city = input("Enter your city: ")

    twist = random.choice([
        f"Hi {name}, you live in {city}. That's awesome!",
        f"Oh wow, {name} from {city}! Sounds like a great place!",
        f"{name}, {city} is lucky to have you!",
        f"Ever thought of coding in {city}, {name}? Bet it's a cool vibe!"
    ])

    print(twist)

if __name__ == "__main__":
    main()
