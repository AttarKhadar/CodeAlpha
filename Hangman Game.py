import random

def hangman():
    # List of words for the game
    words = ["python", "programming", "hangman", "developer", "keyboard", 
             "computer", "algorithm", "function", "variable", "iteration"]
    
    # Select a random word
    secret_word = random.choice(words).upper()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters. You have {attempts} attempts.")
    
    while attempts > 0:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\n" + display_word)
        
        # Check if player has won
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break
        
        # Get player's guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
            
    else:
        print(f"\nGame over! The word was: {secret_word}")
    
    # Ask to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        hangman()
    else:
        print("Thanks for playing!")