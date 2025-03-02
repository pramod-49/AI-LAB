def display_hangman(incorrect_guesses):
    hangman_stages = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
        =========
        '''
    ]
    print(hangman_stages[incorrect_guesses])

def play_game(word_to_guess):
    word_pattern = '_' * len(word_to_guess)
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("Word to guess:", ' '.join(word_pattern))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Correct guess! '{guess}' is in the word.")
            word_pattern = ''.join([guess if word_to_guess[i] == guess else word_pattern[i] for i in range(len(word_to_guess))])
        else:
            print(f"Incorrect guess! '{guess}' is not in the word.")
            incorrect_guesses += 1

        if '_' not in word_pattern:
            display_hangman(incorrect_guesses)
            print(f"Congratulations! You've guessed the word: {word_pattern}")
            break
    else:
        display_hangman(incorrect_guesses)
        print(f"You lost! The word was: {word_to_guess}")

word_to_guess = input("Player 1, please enter the word: ").lower()
play_game(word_to_guess)
