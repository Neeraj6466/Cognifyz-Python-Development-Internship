
# Cognifyz Internship
# Level 2 - Task 1
# Guessing Game

import random

# Generate random number
secret_number = random.randint(1, 100)

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break
