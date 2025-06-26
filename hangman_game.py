import random

# List of predefined words
words = ["apple", "python", "code", "hangman", "banana"]
word = random.choice(words)  # Randomly pick a word

guessed_letters = []         # Store guessed letters
tries = 6                    # Max wrong guesses

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while tries > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    if "_" not in display_word:
        print("🎉 You guessed it right! You win!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
    elif guess in word:
        print("✅ Correct guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        tries -= 1
        print(f"Tries left: {tries}")

if tries == 0:
    print("Game Over! The word was:", word)