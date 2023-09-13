

import random

secret_number = random.randint(0, 10)

max_attempts = 4
attempts = 0

while attempts < max_attempts:
    guess_str = input("Guess the secret number (0-10): ")

    # Check if the user entered nothing (an empty string)
    if guess_str == "":
        print("Please enter a valid number.")
        continue

    guess = int(guess_str)
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if attempts == max_attempts:
    print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")
