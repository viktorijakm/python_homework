def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
                all_guessed = False

        print("Current word:", display)
        return all_guessed

    return hangman_closure

# --- Main game logic ---
if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()  # lowercase for consistent matching
    guess_letter = make_hangman(secret)

    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        completed = guess_letter(guess)
        if completed:
            print("Congratulations! You guessed the word:", secret)
            break