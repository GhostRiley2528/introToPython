class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}: {self.meaning}"


def main():
    flashcards1 = []

    while True:
        word = input("Enter the word (or type 'done' to finish): ")
        if word.lower() == 'done':
            break
        meaning = input("Enter its definition: ")
        card = flashcard(word, meaning)
        flashcards1.append(str(card))

    print("\n--- All Flashcards ---")
    index = 0
    while index < len(flashcards1):
        print(flashcards1[index])
        index += 1


if __name__ == "__main__":
    main()
