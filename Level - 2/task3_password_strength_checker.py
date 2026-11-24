
# Cognifyz Internship
# Level 2 - Task 3
# Password Strength Checker

def check_password(password):

    score = 0

    # Check length
    if len(password) >= 8:
        score = score + 1

    # Check uppercase letter
    if any(char.isupper() for char in password):
        score = score + 1

    # Check lowercase letter
    if any(char.islower() for char in password):
        score = score + 1

    # Check digit
    if any(char.isdigit() for char in password):
        score = score + 1

    # Check special character
    if any(not char.isalnum() for char in password):
        score = score + 1

    # Display result
    if score == 5:
        print("Strong Password!")

    elif score >= 3:
        print("Medium Password!")

    else:
        print("Weak Password!")


# Get password from user
user_password = input("Enter your password: ")

check_password(user_password)
