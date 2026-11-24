
# Cognifyz Internship
# Level 2 - Task 4
# Fibonacci Sequence

print("===== FIBONACCI SEQUENCE =====")

# Get number of terms from user
n = int(input("How many terms do you want? "))

# First two numbers
a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")

else:
    print("Fibonacci Sequence:")

    for i in range(n):
        print(a, end=" ")

        # Calculate next number
        next_number = a + b

        a = b
        b = next_number
