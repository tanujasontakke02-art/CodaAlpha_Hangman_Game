import random

words = ["apple", "mango", "python", "laptop", "school"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha():
        print("❌ Sirf letters enter karo (a-z)!")
        continue

    if len(guess) != 1:
        print("❌ Sirf 1 letter enter karo!")
        continue

    if guess in guessed_letters:
        print("⚠️ Ye letter pehle guess ho chuka hai!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

print("\n-------------------")

if "_" not in guessed_word:
    print("🎉 YOU WIN!")
    print("Word was:", word)
else:
    print("💀 GAME OVER!")
    print("Word was:", word)