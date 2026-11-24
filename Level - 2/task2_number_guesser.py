
# Cognifyz Internship
# Level 2 - Task 2
# Number Guesser

import random

print("===== NUMBER GUESSER GAME =====")

# Get range from user
minimum = int(input("Enter minimum number: "))
maximum = int(input("Enter maximum number: "))

# Check range
if minimum >= maximum:
    print("Invalid range! Minimum must be smaller than maximum.")

else:
    # Generate random number
    secret_number = random.randint(minimum, maximum)

    print("Guess a number between", minimum, "and", maximum)

    while True:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too Low! Try Again.")

        elif guess > secret_number:
            print("Too High! Try Again.")

        else:
            print("Congratulations! Correct Guess!")
            break
