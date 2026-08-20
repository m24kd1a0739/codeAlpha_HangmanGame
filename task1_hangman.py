import random

# Predefined list of words
words = ["python", "computer", "programming", "developer", "github"]

# Select a random word
word = random.choice(words)

# Game settings
guesses_left = 6
guessed_letters = []

print("===================================")
print("          HANGMAN GAME")
print("===================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Create hidden word
display_word = ["_"] * len(word)

while guesses_left > 0 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guesses left:", guesses_left)

    # Get user input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        guesses_left -= 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\n===================================")
    print("Congratulations! You won!")
    print("The word was:", word)
    print("===================================")

else:
    print("\n===================================")
    print("Game Over!")
    print("The word was:", word)
    print("===================================")
