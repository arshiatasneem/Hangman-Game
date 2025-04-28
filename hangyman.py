import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman_multiplayer():
    # Hangman ASCII art (7 stages)
    hangman_art = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    # Player 1 enters the word
    while True:
        secret_word = input("Player 1, enter the word to guess: ").lower()
        if secret_word.isalpha():
            break
        print("❌ Only letters allowed (no numbers/symbols). Try again.")

    clear_screen()  # Hide the word from Player 2

    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("\nPlayer 2, start guessing!")
    print(hangman_art[0])  # Initial hangman stage

    while wrong_guesses < max_attempts:
        # Display the word with blanks (_) for unguessed letters
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord:", display_word)

        # Check if the player has won
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word!")
            break

        # Player 2 guesses a letter
        while True:
            guess = input("\nGuess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("❌ Please enter a single letter.")

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess not in secret_word:
            wrong_guesses += 1
            print(f"❌ Wrong guess! Attempts left: {max_attempts - wrong_guesses}")
            print(hangman_art[wrong_guesses])
        else:
            print("✅ Correct guess!")

    # Game over (if player loses)
    if wrong_guesses == max_attempts:
        print(f"\n💀 Game over! The word was: {secret_word}")
        print(hangman_art[6])  # Full hangman

# Start the game
hangman_multiplayer()
