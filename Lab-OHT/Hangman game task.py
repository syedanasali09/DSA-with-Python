import random

# List of words
words = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'grape', 'pineapple']

def hangman():
    # Select a random word from the list
    word = random.choice(words)
    guessed_letters = []
    tries = 6  # Number of tries before game over

    print("Welcome to Hangman!")
    print("Guess the word by  entering one letter at a time.")
    print("You have 6 tries.")

    while tries > 0:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Prompt for a letter guess
        guess = input("Enter a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the letter to the guessed letters list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    # Check if the player has lost
    if tries == 0:
        print("Game over! You ran out of tries. The word was:", word)

# Start the game
hangman()