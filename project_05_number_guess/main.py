import random

print("🎯Welcome to the number guessing game!")

secret_number = random. randint(1, 10)

guess = 0

while guess != secret_number:
    guess_text = input("Guess a number between 1 and 10:")
    guess = int(guess_text)

    if guess == secret_number:
        print("🎉Correct! You guessed it!")
    else:
        print("❌Wrong! Try again.")
        